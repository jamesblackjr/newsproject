from django import forms
from .models import Feed

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['url']
        labels = {
            'url': 'RSS/Atom URL:'
        }
        widgets = {
            'url': forms.URLInput(attrs={'class': 'form-control'})
        }