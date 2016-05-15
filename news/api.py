from datetime import datetime, timedelta
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Article, Feed
from .pagination import LinkHeaderPagination
from .serializers import ArticleSerializer

class ArticlesList(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def list(self, request, feed_id=None):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
             
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def get_queryset(self):
        queryset = Article.objects.order_by('-publication_date')
        
        if "feed_id" in self.kwargs:
            feed_id = self.kwargs['feed_id']
            feed = Feed.objects.get(pk=feed_id)
            queryset = queryset.filter(feed=feed)
        else:
            queryset = queryset.filter(feed__is_active=True)
            
        days = self.request.query_params.get('days', None)
        
        if days is not None:
            queryset = queryset.filter(publication_date__gte=datetime.now()-timedelta(days=int(days)))
        
        return queryset