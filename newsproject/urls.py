"""newsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from news.api import ArticlesList
from news.views import articles_list

urlpatterns = [
    # Auth URLs
    url(r'^logout/$', auth_views.logout, {'next_page': 'articles-list'}, name='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    
    # Admin URLs
    url(r'^admin/', admin.site.urls),
    
    # Custom URLs
    url(r'^$', articles_list, name='articles-list'),
    url(r'^news/', include('news.urls')),
    
    # REST API URLs
    url(r'^api/news/articles/$', ArticlesList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
