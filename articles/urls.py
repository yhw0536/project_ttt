from django.urls import path

from articles import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_list, name='list'),
    path('<int:articles_id>/', views.articles_detail, name='detail'),
    path('create/', views.articles_create, name='create'),
]
