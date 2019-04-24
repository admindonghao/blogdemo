from django.contrib import admin
from .models import Article,Sort,Labels,Author,Comment

admin.site.site_header = '后台管理系统'
admin.site.site_title = '后台管理'
admin.site.index_title = '后台站点管理'


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','author','create_time']


admin.site.register(Sort)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Labels)

