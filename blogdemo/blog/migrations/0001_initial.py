# Generated by Django 2.2 on 2019-04-23 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='文章')),
                ('author', models.CharField(max_length=30, verbose_name='作者')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('reads', models.IntegerField(default=0, verbose_name='浏览数')),
                ('count', models.TextField(verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(max_length=50, verbose_name='类别名称')),
            ],
            options={
                'verbose_name_plural': '类别',
            },
        ),
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.CharField(max_length=10, verbose_name='标签名')),
                ('aet', models.ManyToManyField(null=True, to='blog.Article', verbose_name='文章')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='评论人')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('website', models.URLField(verbose_name='网址')),
                ('count', models.CharField(max_length=200, verbose_name='内容')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='文章id')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='sort_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Sort', verbose_name='分类'),
        ),
    ]
