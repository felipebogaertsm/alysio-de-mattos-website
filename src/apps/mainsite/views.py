# -*- coding: utf-8 -*-
# Author: Felipe Bogaerts de Mattos
# Contact me at felipe.bogaerts@engenharia.ufjf.br.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.

from django.shortcuts import render
from .models import MyBow

# Create your views here.


def home(request):
    return render(request, "mainsite/index.html")


def aboutme(request):
    return render(request, "mainsite/aboutme.html")


def wood(request):
    return render(request, "mainsite/wood.html")


def gallery(request):
    bows = MyBow.objects.all()
    return render(request, "mainsite/gallery.html", {"bows": bows})


def contact(request):
    return render(request, "mainsite/contact.html")
