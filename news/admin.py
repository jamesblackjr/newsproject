from django.template.defaultfilters import escape
from django.core.urlresolvers import reverse
from django.contrib import admin
from .models import Feed, Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):    
    def feed_link(self, obj):
        return '<a href="%s">%s</a>' % (reverse("admin:news_feed_change", args=(obj.feed.id,)) , escape(obj.feed))
        
    def date_display(self, obj):
        return obj.publication_date.strftime('%Y-%m-%d %H:%M:%S')
    
    feed_link.allow_tags = True
    feed_link.short_description = "Feed"    
    date_display.short_description = "Publication Date"
        
    list_display = ("title", "feed_link", "date_display",)
    list_display_links = ("title",)
    list_filter = ("publication_date",)
    search_fields = ("title",)
    
@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):    
    list_display = ("title", "url", "is_active",)
    list_editable = ("is_active",)
    list_display_links = ("title",)
    list_filter = ("is_active",)
    search_fields = ("title",)