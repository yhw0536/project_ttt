from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core import exceptions
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from articles.forms import ArticlesForm
from articles.models import Article


# Create your views here.

def articles_list(request: HttpRequest):
    search_keyword = request.GET.get('search_keyword', '')

    if not search_keyword:
        articles = Article.objects.order_by('-id')
    else:
        articles = Article.objects.filter(Q(title__icontains=search_keyword)
                                          | Q(content__icontains=search_keyword)
                                          | Q(tag__icontains=search_keyword)).order_by('-id')

    page = int(request.GET.get('page', 1))
    paginator = Paginator(articles, 6)
    a_list = paginator.get_page(page)

    return render(request, "articles/articles_list.html", {
        "articles": a_list
    })


def articles_detail(request: HttpRequest, articles_id):
    articles = get_object_or_404(Article, id=articles_id)

    return render(request, "articles/articles_detail.html", {
        "articles": articles,
    })


def articles_create(request):
    form = ArticlesForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            article = form.save(commit=False)
            article.content_type = ContentType.objects.get_for_model(article)
            article.object_id = article.id
            article.user_id = request.user.id
            article.username = request.user.username
            article.img = article.img
            article.save()
            messages.success(request, "포스트 작성이 완료되었습니다.")

            return redirect("articles:list")
    else:
        form = ArticlesForm()
        return render(request, "articles/articles_create.html",
                      {'form': form})


@login_required
def articles_delete(request: HttpRequest, articles_id):
    articles = get_object_or_404(Article, id=articles_id)

    if request.user != articles.user:
        raise exceptions.PermissionDenied()

    articles.delete()

    messages.success(request, "포스트가 삭제되었습니다.")

    return redirect("articles:list")


@login_required
def articles_modify(request, articles_id):
    """질문수정"""
    articles = get_object_or_404(Article, pk=articles_id)
    if request.user != articles.user:
        messages.error(request, '수정권한이 없습니다')
        return redirect('articles:detail', articles_id=articles.id)

    if request.method == "POST":
        form = ArticlesForm(request.POST, instance=articles)
        if form.is_valid():
            articles = form.save(commit=False)
            articles.user = request.user
            articles.modify_date = timezone.now()  # 수정일시 저장
            articles.save()
            return redirect('articles:detail', articles_id=articles.id)
    else:
        form = ArticlesForm(instance=articles)
    return render(request, 'articles/articles_create.html',
                  {'form': form})


@login_required
def vote_articles(request, articles_id):
    articles = get_object_or_404(Article, pk=articles_id)
    if request.user == articles.user:
        messages.warning(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        articles.voter.add(request.user)
    return redirect('articles:list')
