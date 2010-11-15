# -*- coding: utf-8 -*-
from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Название')
    url = models.CharField(max_length = 400, verbose_name = 'Адрес')
    parent = models.ForeignKey('self', verbose_name = 'Родитель', blank = True, null=True)
    popup = models.BooleanField(verbose_name = 'Открыть в сплывающем окне?')
    tab = models.BooleanField(verbose_name = 'Открыть в новой вкладке?')
    
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
    
    def __unicode__(self):
        return self.title