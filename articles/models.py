from django_summernote.fields import SummernoteTextField

from accounts.models import User
from django.db import models


# Create your models here.


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_articles')
    reg_date = models.DateField('등록날짜', auto_now_add=True)
    update_date = models.DateField('수정날짜', auto_now=True)
    delete_date = models.DateField('삭제날짜', null=True, blank=True)
    is_deleted = models.BooleanField('삭제여부', default=False)
    title = models.CharField('제목', max_length=100)
    content = models.TextField('내용')
    contry = models.CharField('나라', max_length=100)
    city = models.CharField('도시', max_length=100)
    tag = models.CharField('태그', max_length=300, null=True, blank=True)
    hit_count = models.PositiveIntegerField('조회수', default=0)
    review_count = models.PositiveIntegerField('리뷰수', default=0)
    review_point = models.PositiveIntegerField('리뷰평점', default=0)
    img = models.ImageField('이미지', blank=True, upload_to="media/%Y/%m/%d")
    voter = models.ManyToManyField(User, related_name='voter_articles')

    def __str__(self):
        return self.title
