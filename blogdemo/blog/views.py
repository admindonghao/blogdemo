from django.shortcuts import render, reverse, redirect
from .models import Article, Author, Sort, Labels, Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
import markdown


# Create your views here.

# 主页
def index(request):
    articles = Article.objects.all()
    # 分页用到的代码
    paginator = Paginator(articles, 4, 2)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'articles':articles})


# 详情页
def single(request, id):
    if request.method == 'GET':
        article = Article.objects.get(pk=id)
        article.count = markdown.markdown(article.count,extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        ])
        return render(request, 'blog/single.html', {'article':article})
    elif request.method == 'POST':
        comment = Comment()
        comment.name = request.POST['name']
        comment.email = request.POST['email']
        comment.website = request.POST['url']
        comment.count = request.POST['comment']
        comment.article_id = Article.objects.get(pk=id)
        comment.save()
        # return HttpResponseRedirect('/blog/single/{}'.format(id))
        return redirect(reverse('blog:single', args=(id,)))


# 归档
def archive(request, year, month):
    articles = Article.objects.filter(create_time__year=year).filter(create_time__month=month)
    # 分页用到的代码
    paginator = Paginator(articles, 4, 2)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'articles': articles})
    # return HttpResponse('omom')


# 分类
def sort(request, id):
    articles = Sort.objects.get(pk=id).article_set.all()
    # 分页用到的代码
    paginator = Paginator(articles, 4, 2)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'articles': articles})


# 标签
def labels(request,id):
    articles = Labels.objects.get(pk=id).article_set.all()
    # 分页用到的代码
    paginator = Paginator(articles, 4, 2)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'articles': articles})
