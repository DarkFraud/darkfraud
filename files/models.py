# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save, pre_delete
from darkfraud.utils import *

class Image(models.Model):
    title = models.CharField(max_length = 250, verbose_name = 'Название')
    image = models.ImageField(upload_to = 'images/Images/', verbose_name = 'Изображение')
    
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

class File(models.Model):
    title = models.CharField(max_length = 250, verbose_name = 'Название')
    file = models.ImageField(upload_to = 'images/Files/', verbose_name = 'Файл')
    
    class Meta:
        verbose_name_plural = 'Файлы'
        verbose_name = 'Файл'
    
    def __unicode__(self):
        return self.title