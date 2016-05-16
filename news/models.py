from django.db import models
from time import mktime
import datetime, feedparser

# Create your models here.
class Feed(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(unique=True, help_text="Don't forget to add http:// or https:// to the URL")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        # Check to see if this is a new feed or not
        new_feed = self.pk is None
        
        feed_data = feedparser.parse(self.url)
        
        # Set feed title field if available
        if new_feed:
            if feed_data.feed.title:
                self.title = feed_data.feed.title
            else:
                self.title = "Undefined"
            
        super(Feed, self).save(*args, **kwargs)
        
        if new_feed:
            self.get_feed_articles()

    def get_feed_articles(self):
        feed_data = feedparser.parse(self.url)
        
        for entry in feed_data.entries:
            try:
                article = Article.objects.get(url=entry.link)
            except:
                article = Article()
            
            article.title = entry.title
            article.url = entry.link
            article.description = entry.description

            # Set publication date
            try:
                published = entry.published_parsed
            except AttributeError:
                try:
                    published = entry.updated_parsed
                except AttributeError:
                    published = entry.created_parsed
            
            publication_date = datetime.datetime.fromtimestamp(mktime(published))
            date_string = publication_date.strftime('%Y-%m-%d %H:%M:%S')
            article.publication_date = date_string

            article.feed = self
            article.save()
    
class Article(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=200)
    url = models.URLField(verbose_name="URL")
    description = models.TextField()
    publication_date = models.DateTimeField()
    
    def __str__(self):
        return self.title