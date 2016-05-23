from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    feed = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(max_length=200)
    url = serializers.URLField()
    description = serializers.CharField(source='description_truncated')
    publication_date = serializers.DateTimeField(format='%A %B %d, %Y %-I:%M %p')
