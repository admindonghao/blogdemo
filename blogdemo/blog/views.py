from django.shortcuts import render, reverse, redirect
from .models import Article, Author, Sort, Labels, Comment
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect


# Create your views here.
def index(request):
    articles = Article.objects.all()
    articless = Article.objects.all()[:3]
    sorts = Sort.objects.all()
    labelss = Labels.objects.all()
    dates = Article.objects.datetimes('create_time', 'month', order='DESC')
    # print(dates)
    return render(request, 'blog/index.html', {'articles':articles, 'articless':articless, 'sorts':sorts,
                                               'labelss':labelss, 'dates':dates})


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

