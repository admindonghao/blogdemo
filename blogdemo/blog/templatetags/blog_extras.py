from django import template
from ..models import Article,Author,Sort,Labels,Comment
# 得到Django负责管理标签和过滤器的类
register = template.Library()


# 最新文章
@register.simple_tag
def get_articless():
    articless = Article.objects.all()[:3]
    return articless


# 分类
@register.simple_tag
def get_sorts():
    sorts = Sort.objects.all()
    return sorts


# 标签云
@register.simple_tag
def get_labelss():
    labelss = Labels.objects.all()
    return labelss


# 归档显示
@register.simple_tag
def get_dates():
    dates = Article.objects.datetimes('create_time', 'month', order='DESC')
    return dates

