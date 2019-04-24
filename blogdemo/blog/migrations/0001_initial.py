# Generated by Django 2.2 on 2019-04-24 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='作者')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('plone', models.IntegerField(max_length=11, verbose_name='手机号')),
            ],
            options={
                'verbose_name_plural': '作者表',
            },
        ),
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.CharField(max_length=10, verbose_name='标签名')),
            ],
            options={
                'verbose_name_plural': '标签表',
            },
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
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='文章')),
                ('reads', models.IntegerField(default=0, verbose_name='浏览数')),
                ('summany', models.TextField(verbose_name='文章摘要')),
                ('count', models.TextField(verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Author', verbose_name='作者')),
                ('label', models.ManyToManyField(to='blog.Labels', verbose_name='标签')),
                ('sort_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Sort', verbose_name='分类')),
            ],
            options={
                'verbose_name_plural': '文章表',
                'ordering': ['-create_time'],
            },
        ),
    ]
