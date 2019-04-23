from django.db import models


# Create your models here.
# 创建blog应用生成表的类
# 创建分类表的类
class Sort(models.Model):
    """
    classname   类别名称
    """
    classname = models.CharField(max_length=50, verbose_name='类别名称')

    def __str__(self):
        return self.classname

    class Meta:
        verbose_name_plural = '类别'


# 创建文章表的类
class Article(models.Model):
    """
    title   文章名称;  author  作者;  datetime  时间（自动获取）;
    sort_id  分类 (外键);   reads  浏览数（默认为0）; count  内容
    """
    title = models.CharField(max_length=50, verbose_name='文章')
    author = models.CharField(max_length=30, verbose_name='作者')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='时间')
    reads = models.IntegerField(default=0, verbose_name='浏览数')
    count = models.TextField(verbose_name='内容')
    sort_id = models.ForeignKey(Sort, on_delete=models.CASCADE, verbose_name='分类')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '文章表'


# 创建评论表的类
class Comment(models.Model):
    """
    name   评论人; email   邮箱; website  网址;count   内容
    article_id   外键（文章id）
    """
    name = models.CharField(max_length=30, verbose_name='评论人')
    email = models.EmailField(verbose_name='邮箱')
    website = models.URLField(verbose_name='网址')
    count = models.CharField(max_length=200, verbose_name='内容')
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章id')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '评论表'


# 创建标签表的类
class Labels(models.Model):
    """
    label_name  标签名;
    art     文章（多对多关系）
    """
    label_name = models.CharField(max_length=10, verbose_name='标签名')
    aet = models.ManyToManyField(Article, null=True, verbose_name='文章')

    def __str__(self):
        return self.label_name

    class Meta:
        verbose_name_plural = '标签表'
