# -*- coding: utf-8 -*-
from django.contrib import admin
from darkfraud.menu.models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent', 'popup', 'tab',)
    ordering = 'parent',
    fieldsets = (
        ('Меню', {
            'classes': ['wide', 'extrapretty'],
            'fields': ('title', 'url', 'parent', 'popup', 'tab',)
        }),
    )
    
admin.site.register(Menu, MenuAdmin)