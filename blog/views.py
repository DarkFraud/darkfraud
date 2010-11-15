# -*- coding: utf-8 -*-
import datetime, time
from django.core.mail import send_mail
from django.db.models import Q
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponseRedirect
from darkfraud.blog.models import Category, Tag, Post, Comment
from darkfraud.menu.models import Menu

from django import forms
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm

def home(request):
    menu = Menu.objects.all().order_by('id')
    posts = Post.objects.filter(status = 1).order_by('-pub_date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    arhive = Post.objects.dates('pub_date', 'month')
    
    paginator = Paginator(posts, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    
    return direct_to_template(request, 'blog/home.html', locals())
    
def category(request, slug):
    menu = Menu.objects.all()
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories = category, status = 1).order_by('-pub_date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    arhive = Post.objects.dates('pub_date', 'month')
    
    paginator = Paginator(posts, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    
    return direct_to_template(request, 'blog/home.html', locals())
    
def tag(request, slug):
    menu = Menu.objects.all()
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags = tag, status = 1).order_by('-pub_date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    arhive = Post.objects.dates('pub_date', 'month')
    
    paginator = Paginator(posts, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    
    return direct_to_template(request, 'blog/home.html', locals())
    
def post(request, year, month, day, slug):
    menu = Menu.objects.all()
    date_stamp = time.strptime(year+month+day, "%Y%m%d")
    pub_date = datetime.date(*date_stamp[:3])
    post = get_object_or_404(Post, pub_date__year=pub_date.year, pub_date__month=pub_date.month, pub_date__day=pub_date.day, slug=slug, status=1)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    arhive = Post.objects.dates('pub_date', 'month')
    coments = Comment.objects.filter(post=post).order_by('-pub_date')
    if request.POST:
        comment_text = request.POST['text_comment']
        if len(comment_text)<3: return HttpResponseRedirect(request.path)
        author = request.user
        post_id = post
        db = Comment(status=1, comment=comment_text, author=author, post=post_id, pub_date=datetime.datetime.now())
        db.save()
        '''
        send_mail(
            'Новый коментарий',
            db.comment,
            'darkfraud@gmail.com',
            ['darkfraud@gmail.com'],
        )
        '''
        return HttpResponseRedirect(request.path+'#comment')
    return direct_to_template(request, 'blog/post.html', locals())
    
def arhive(request, year, month):
    menu = Menu.objects.all()
    date_stamp = time.strptime(year+month+str(12), "%Y%m%d")
    pub_date = datetime.date(*date_stamp[:3])
    posts = Post.objects.filter(status=1, pub_date__year=pub_date.year, pub_date__month=pub_date.month)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    arhive = Post.objects.dates('pub_date', 'month')
    
    paginator = Paginator(posts, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    
    return direct_to_template(request, 'blog/home.html', locals())
    
def register(request):
    menu = Menu.objects.all()
    form = UserCreationForm()
    if request.method == 'POST':
        data = request.POST.copy()
        form = UserCreationForm(data)
        if form.is_valid():
            new_user = form.save(data)
            '''
            send_mail(
                'Новый пользователь',
                new_user,
                'darkfraud@gmail.com',
                ['darkfraud@gmail.com'],
            )
            '''
            return HttpResponseRedirect("/accounts/login/")
    else:
        data, errors = {}, {}
    return direct_to_template(request, 'registration/register.html', locals())
    
def profile(request):
    return HttpResponseRedirect('/')
    
def search(request):
    # Наполнители
    menu = Menu.objects.all()
    posts = Post.objects.filter(status = 1).order_by('-pub_date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    arhive = Post.objects.dates('pub_date', 'month')
    # Поиск
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
        posts = Post.objects.filter(qset).distinct()
    # Пагинатор
    paginator = Paginator(posts, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    
    return direct_to_template(request, 'blog/home.html', locals())