from django.shortcuts import redirect, render
from .models import Article, Feed
from .forms import FeedForm

# Create your views here.
def articles_list(request):
    articles = Article.objects.filter(feed__is_active=True).order_by('-publication_date')
    
    def split_seq(seq, size):
        newseq = []
        splitsize = 1.0/size*len(seq)
        for i in range(size):
                newseq.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])
        return newseq
    
    columns = split_seq(articles, 3)
    
    context = {
        'columns': columns,
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
            feed.save()
                
            return redirect('feeds-list')
    else:
        form = FeedForm
    
    context = {
        'form': form,
    }
    
    return render(request, "new_feed.html", context)