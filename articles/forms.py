from django import forms

from articles.models import Article


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'tag', 'content']
        labels = {
            'title': '제목',
            'tag': '태그',
            'content': '내용',
        }