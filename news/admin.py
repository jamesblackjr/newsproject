from django.contrib import admin
from .models import Feed, Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    def date_display(self, obj):
        return obj.publication_date.strftime('%Y-%m-%d %H:%M:%S')
        
    date_display.short_description = "Publication Date"
        
    list_display = ("title", "date_display",)
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