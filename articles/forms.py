from django import forms
from django_summernote.widgets import SummernoteWidget
from django_summernote.fields import SummernoteTextField

from articles.models import Article


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'tag',
            'content'
        ]

        widgets = {
            'content': SummernoteWidget()
        }

        title = forms.CharField(
            label='제목',
            widget = forms.TextInput(
                attrs={
                    'placeholder': '제목'
                }),
            required=True,
        )

        content = SummernoteTextField()

        field_order = [
            'title',
            'tag',
            'content'
        ]

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title', '')
        content = cleaned_data.get('content', '')

        if title == '':
            self.add_error('title', '제목을 입력하세요.')
        elif content == '':
            self.add_error('content', '내용을 입력하세요')
        else:
            self.title = title
            self.content = content