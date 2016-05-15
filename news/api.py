from rest_framework import generics, status
from rest_framework.response import Response
from .models import Article
from .pagination import LinkHeaderPagination
from .serializers import ArticleSerializer

class ArticlesList(generics.ListAPIView):
    queryset = Article.objects.filter(feed__is_active=True).order_by('-publication_date')
    serializer_class = ArticleSerializer

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        
        if page is not None:
             serializer = self.get_serializer(page, many=True)
             return self.get_paginated_response(serializer.data)
             
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)