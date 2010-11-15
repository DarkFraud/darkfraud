# -*- coding: utf-8 -*-
from django.contrib import admin
from darkfraud.pages.models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)
    ordering = 'id',
    fieldsets = (
        ('Страница', {
            'classes': ['wide', 'extrapretty'],
            'fields': ('title', 'content',)
        }),
    )
    
admin.site.register(Page, PageAdmin)