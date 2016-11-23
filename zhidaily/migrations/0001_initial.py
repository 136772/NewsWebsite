# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 10:44
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('intro', models.CharField(max_length=1000)),
                ('abstract', models.TextField()),
                ('content', models.TextField()),
                ('publish_time', models.DateTimeField(default=datetime.datetime(2016, 11, 19, 10, 44, 21, 124997))),
                ('image', models.FileField(upload_to='article_image')),
                ('source_link', models.CharField(max_length=200)),
                ('author_name', models.CharField(max_length=100)),
                ('author_avatar', models.FileField(upload_to='author_avatar')),
                ('author_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Best',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_reason', models.CharField(choices=[('今日新闻', '今日新闻'), ('首页推荐', '首页推荐'), ('编辑推荐', '编辑推荐')], max_length=50)),
                ('select_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='select_article', to='zhidaily.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=datetime.datetime(2016, 11, 19, 10, 44, 21, 127595))),
                ('belong_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to='zhidaily.Article')),
                ('belong_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.FileField(upload_to='avatar')),
                ('belong_to', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cate', to='zhidaily.Category'),
        ),
    ]
