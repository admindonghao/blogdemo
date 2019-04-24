from django.shortcuts import render
from .models import Article, Author, Sort, Labels


# Create your views here.
def index(request):
    articles = Article.objects.all()
    articless = Article.objects.all()[:3]
    sorts = Sort.objects.all()
    labelss = Labels.objects.all()
    dates = Article.objects.datetimes('create_time', 'month', order='DESC')
    print(dates)
    return render(request, 'blog/index.html', {'articles':articles, 'articless':articless, 'sorts':sorts,
                                               'labelss':labelss, 'dates':dates})


def single(request):
    return render(request, 'blog/single.html')


