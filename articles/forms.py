from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Article


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'tag', 'content']
        widgets = {
            'content': SummernoteWidget()
        }