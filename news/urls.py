from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.articles_list, name='articles-list'),
    url(r'^articles/$', views.articles_list, name='articles-list'),
    url(r'^feeds/new/$', views.new_feed, name='new-feed'),
    url(r'^feeds/(?P<feed_id>[0-9]+)/$', views.articles_list, name='feed-articles'),
    url(r'^feeds/$', views.feeds_list, name='feeds-list'),
]