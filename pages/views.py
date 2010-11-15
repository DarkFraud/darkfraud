# -*- coding: utf-8 -*-
import datetime, time
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from darkfraud.pages.models import Page
from darkfraud.menu.models import Menu

def page(request, id):
    menu = Menu.objects.all().order_by('id')
    page = get_object_or_404(Page, id=id)
    return direct_to_template(request, 'pages/page.html', locals())