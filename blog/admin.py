# -*- coding: utf-8 -*-
from django.contrib import admin
from darkfraud.blog.models import Category, Tag, Post, Comment, Image

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Tag, TagAdmin)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'pub_date'
    filter_horizontal = ('tags', 'categories',)
    list_display = ('title', 'status', 'enable_comments',)
    search_fields = ('title', 'content',)
    fieldsets = (
        ('Пост', {
            'classes': ['wide', 'extrapretty'],
            'fields': ('status', 'title', 'slug', 'content', 'author', 'categories', 'tags', 'enable_comments',)
        }),
        ('Дата публикации', {'fields': ['pub_date',], 'classes': ['collapse']}),
    )

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Пост', {
            'classes': ['wide', 'extrapretty'],
            'fields': ('status', 'author', 'post', 'comment',)
        }),
        ('Дата публикации', {'fields': ['pub_date',], 'classes': ['collapse']}),
    )

admin.site.register(Comment, CommentAdmin)

class ImageAdmin(admin.ModelAdmin):
    class Media:
        js = [
            'javascript/admin/tiny_django_browser.js',
            'javascript/admin/display_thumbs.js',
            ]
    list_display = ['title', 'get_thumbnail_html']
    
admin.site.register(Image, ImageAdmin)