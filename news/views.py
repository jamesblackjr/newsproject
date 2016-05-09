from django.shortcuts import redirect, render
from .models import Article, Feed
from .forms import FeedForm
import datetime, feedparser

# Create your views here.
def articles_list(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles,
    }
    
    return render(request, "articles_list.html", context)
    
def feeds_list(request):
    feeds = Feed.objects.all()
    
    context = {
        'feeds': feeds,
    }
    
    return render(request, "feeds_list.html", context)
    
def new_feed(request):
    if request.method == "POST":
        # Process our form
        form = FeedForm(request.POST)
        
        if form.is_valid():
            feed = form.save(commit=False)
            
            feed_data = feedparser.parse(feed.url)
            
            # Set some fields
            feed.title = feed_data.feed.title
            feed.url = form.cleaned_data['url']
            feed.save()
            
            for entry in feed_data.entries:
                article = Article()
                article.title = entry.title
                article.url = entry.link
                article.description = entry.description
                
                # Set publication date
                publication_date = datetime.datetime(*(entry.published_parsed[0:6]))
                date_string = publication_date.strftime('%Y-%m-%d %H:%M%:%S')
                article.publication_date = date_string
                
                article.feed = feed
                article.save()
                
            return redirect('feeds-list')
    else:
        form = FeedForm
    
    context = {
        'form': form,
    }
    
    return render(request, "new_feed.html", context)