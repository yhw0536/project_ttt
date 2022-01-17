from django.urls import path

from articles import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_list, name='list'),
    path('articles/<int:articles_id>/', views.articles_detail, name='detail'),
    path('articles/modify/<int:articles_id>/', views.articles_modify, name='modify'),
    path('create/', views.articles_create, name='create'),
]
