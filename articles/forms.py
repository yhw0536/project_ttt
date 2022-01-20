from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Article


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'tag', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(ArticlesForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['tag'].label = '태그'
        self.fields['tag'].widget.attrs.update({
            'placeholder': '태그의 앞에는 #을 붙여주세요.',
            'class': 'form-control',
            'autofocus': True,
        })

