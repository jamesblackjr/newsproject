from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from rest_framework import generics, status
from .models import Feed
from .forms import FeedForm

# Create your views here.
def articles_list(request, feed_id=None):
    if feed_id is not None:
        feed = Feed.objects.get(pk=feed_id)
    else:
        feed = None
    
    form = FeedForm
        
    context = {
        'feed': feed,
        'form': form,
    }
    
    return render(request, "articles_list.html", context)

def feeds_list(request):
    feeds = Feed.objects.all()
    form = FeedForm
    
    context = {
        'feeds': feeds,
        'form': form,
    }
    
    return render(request, "feeds_list.html", context)
    
@login_required
def new_feed(request):
    if request.method == "POST":
        # Process our form
        form = FeedForm(request.POST)
        
        if form.is_valid():
            feed = form.save(commit=False)
            feed.save()
                
            return redirect('feeds-list')
    else:
        form = FeedForm
    
    context = {
        'form': form,
    }
    
    return render(request, "new_feed.html", context)