from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article, Feed
from .serializers import ArticleSerializer
from .forms import FeedForm

# Create your views here.
def articles_list(request):
    articles_list = Article.objects.filter(feed__is_active=True).order_by('-publication_date')
    paginator = Paginator(articles_list, 100) # Show 100 articles per page
    
    page = request.GET.get('page')
    
    try:
       articles = paginator.page(page)
    except PageNotAnInteger:
       # If page is not an integer, deliver first page.
       articles = paginator.page(1)
    except EmptyPage:
       # If page is out of range (e.g. 9999), deliver last page of results.
       articles = paginator.page(paginator.num_pages)
    
    context = {
        'articles': articles,
    }
    
    return render(request, "articles_list.html", context)
    
class ArticlesList(APIView):
    def get(self, request, format=None):
        articles = Article.objects.filter(feed__is_active=True).order_by('-publication_date')
        paginator = Paginator(articles, 100)
        page = request.GET.get('page')
        
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            articles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            articles = paginator.page(paginator.num_pages)
        
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


@login_required   
def feeds_list(request):
    feeds = Feed.objects.all()
    
    context = {
        'feeds': feeds,
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