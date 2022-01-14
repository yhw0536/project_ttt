from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.utils import timezone

from articles.forms import ArticlesForm
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


def articles_detail():
    return None


def articles_create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            article = form.save()
            article.content_type = ContentType.objects.get_for_model(article)
            article.object_id = article.id
            article.user_id = request.user.id
            article.save()
            messages.success(request, "포스트 작성이 완료되었습니다.")

            return redirect("articles:list")
    else:
        form = ArticlesForm()
        return render(request, "articles/articles_create.html",
                      {'form': form})