# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from darkfraud.utils import *

class Category(models.Model):
    title = models.CharField(max_length = 250, verbose_name = 'Название')
    slug = models.SlugField(unique=True, verbose_name = 'Арес')
    description = models.TextField(verbose_name = 'Описание')
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
    
    def __unicode__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length = 250, verbose_name = 'Название')
    slug = models.SlugField(unique=True, verbose_name = 'Арес')
    
    class Meta():
        ordering = ['title']
        verbose_name_plural = 'Тэги'
        verbose_name = 'Тэг'
    
    def __unicode__(self):
        return self.title

class Post(models.Model):
    STATUS_CHOICES = (
        (1, 'Открыто'),
        (2, 'Закрыто'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name = 'Статус')
    title = models.CharField(max_length = 250, verbose_name = 'Название')
    pub_date = models.DateTimeField(default = datetime.datetime.now, verbose_name = 'Дата')
    slug = models.SlugField(unique_for_date = 'pub_date', verbose_name = 'Арес')
    content = models.TextField(verbose_name = 'Контент')
    author = models.ForeignKey(User, verbose_name ='Автор')
    categories = models.ManyToManyField(Category)#, verbose_name ='Категории')
    tags = models.ManyToManyField(Tag)#, verbose_name ='Теги')
    enable_comments = models.BooleanField(default = True, verbose_name ='Позволить коментировать')
    
    class Meta():
        ordering = ['-pub_date']
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'
    
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    STATUS_CHOICES = (
        (1, 'Открыто'),
        (2, 'Закрыто'),
    )
    status = models.IntegerField(choices = STATUS_CHOICES, default = 2, verbose_name ='Статус')
    comment = models.TextField(verbose_name = 'Коментарий')
    author = models.ForeignKey(User, verbose_name = 'Автор')
    post = models.ForeignKey(Post, verbose_name = 'Пост')
    pub_date = models.DateTimeField(default = datetime.datetime.now, verbose_name='Дата')
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = 'Коментарий'
        verbose_name = 'Коментарий'
    
    def __unicode__(self):
        return self.post.title

class Image(models.Model):
    title = models.CharField(max_length = 250, verbose_name = 'Название')
    image = models.ImageField(upload_to = 'images/Blog/', verbose_name = 'Изображение')
    
    class Meta:
        verbose_name_plural = 'Изображения'
        verbose_name = 'Изобрвжение'
    
    def __unicode__(self):
        return self.title
    
    def get_thumbnail_html(self):
        html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
        return html % (self.image.url, get_thumbnail_url(self.image.url), self.title)
    get_thumbnail_html.short_description = 'Изображение'
    get_thumbnail_html.allow_tags = True

def post_save_handler(sender, **kwargs):
    create_thumbnail(kwargs['instance'].image.path)
post_save.connect(post_save_handler, sender=Image)

def pre_delete_handler(sender, **kwargs):
    delete_thumbnail(kwargs['instance'].image.path)
pre_delete.connect(pre_delete_handler, sender=Image)