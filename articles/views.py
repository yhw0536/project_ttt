from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from articles.models import Article


# Create your views here.

def articles_list(request: HttpRequest):
    search_keyword = request.GET.get('search_keyword', '')

    if not search_keyword:
        products = Article.objects.order_by('-id')
    else:
        products = Article.objects.filter(title__icontains=search_keyword).order_by('-id')

    page = int(request.GET.get('page', 1))
    paginator = Paginator(products, 4)
    a_list = paginator.get_page(page)

    return render(request, "articles/articles_list.html", {
        "articles": a_list
    })


