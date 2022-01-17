from django.urls import path

from articles import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_list, name='list'),
    path('<int:articles_id>/', views.articles_detail, name='detail'),
    path('modify/<int:articles_id>/', views.articles_modify, name='modify'),
    path('delete/<int:articles_id>/', views.articles_delete, name='delete'),
    path('create/', views.articles_create, name='create'),
]
