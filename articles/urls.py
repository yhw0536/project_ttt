from django.urls import path

from articles import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_list, name='list'),
    path('', views.articles_detail, name='detail'),
]
