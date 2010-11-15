# -*- coding: utf-8 -*-
from django.db import models

class Page(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Название')
    content = models.TextField(verbose_name = 'Контент')
    
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
    
    def __unicode__(self):
        return self.title