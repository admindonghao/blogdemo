from django.contrib import admin
from .models import Article,Sort,Comment,Labels


# Register your models here.
admin.site.register(Sort)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Labels)

