from django.db import models

# Create your models here.

class Article(models.Model):
    reg_date = models.DateField('등록날짜', auto_now_add=True)
    update_date = models.DateField('수정날짜', auto_now=True)
    delete_date = models.DateField('삭제날짜', null=True, blank=True)
    is_deleted = models.BooleanField('삭제여부', default=False)
    title = models.CharField('제목', max_length=100)
    content = models.TextField('내용')
    contry = models.CharField('나라', max_length=100)
    city = models.CharField('도시', max_length=100)