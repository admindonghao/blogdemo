from django.contrib.syndication.views import Feed
from .models import Article
from django.shortcuts import reverse


class RssFeed(Feed):
    title = '文章'
    description = '文章摘要'
    link = '/'

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summany

    def item_link(self, item):
        return reverse('blog:single', args=(item.id,))
