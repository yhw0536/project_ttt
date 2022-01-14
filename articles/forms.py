from django import forms

from articles.models import Article


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']