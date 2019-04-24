from django.shortcuts import render, reverse, redirect
from .models import Article, Author, Sort, Labels, Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.
# 主页
def index(request):
    articles = Article.objects.all()
    articless = Article.objects.all()[:3]
    sorts = Sort.objects.all()
    labelss = Labels.objects.all()
    # 归档显示所需的截止到月份的时间对象集
    dates = Article.objects.datetimes('create_time', 'month', order='DESC')
    # 分页用到的代码
    paginator = Paginator(articles, 4, 2)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'articles':articles, 'articless':articless, 'sorts':sorts,
                                               'labelss':labelss, 'dates':dates})


# 详情页
def single(request, id):
    if request.method == 'GET':
        article = Article.objects.get(pk=id)
        articless = Article.objects.all()[:3]
        sorts = Sort.objects.all()
        labelss = Labels.objects.all()
        dates = Article.objects.datetimes('create_time', 'month', order='DESC')
        return render(request, 'blog/single.html', {'article':article, 'articless':articless, 'sorts':sorts,
                                                    'labelss':labelss, 'dates':dates})
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
def archive(request, month, year):
    pass


