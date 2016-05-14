from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.articles_list, name='articles-list'),
    url(r'^feeds/new', views.new_feed, name='new-feed'),
    url(r'^feeds/', views.feeds_list, name='feeds-list'),
    
    # REST Api URLs
    url(r'^api/articles/$', views.ArticlesList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)