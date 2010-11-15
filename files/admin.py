# -*- coding: utf-8 -*-
from django.contrib import admin
from darkfraud.files.models import Image, File

class ImageAdmin(admin.ModelAdmin):
    class Media:
        js = [
            'javascript/admin/tiny_django_browser.js',
            'javascript/admin/display_thumbs.js',
            ]
    list_display = ['title', 'get_thumbnail_html']
    
admin.site.register(Image, ImageAdmin)

admin.site.register(File)