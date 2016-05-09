from django.db import models
import datetime, feedparser

# Create your models here.
class Feed(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        feed_data = feedparser.parse(self.url)
        
        # Set some fields
        self.title = feed_data.feed.title
            
        super(Feed, self).save(*args, **kwargs)
        
        for entry in feed_data.entries:
            article = Article()
            article.title = entry.title
            article.url = entry.link
            article.description = entry.description
            
            # Set publication date
            publication_date = datetime.datetime(*(entry.published_parsed[0:6]))
            date_string = publication_date.strftime('%Y-%m-%d %H:%M%:%S')
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