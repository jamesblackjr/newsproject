from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Article, Feed
from .pagination import LinkHeaderPagination
from .serializers import ArticleSerializer
from .forms import FeedForm

# Create your views here.
def articles_list(request):    
    return render(request, "articles_list.html")
    
class ArticlesList(generics.ListCreateAPIView):
    queryset = Article.objects.filter(feed__is_active=True).order_by('-publication_date')
    serializer_class = ArticleSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        
        if page is not None:
             serializer = self.get_serializer(page, many=True)
             return self.get_paginated_response(serializer.data)
             
        serializer = ArticleSerializer(queryset, many=True)
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