# -*- coding: utf-8 -*-
# Author: Felipe Bogaerts de Mattos
# Contact me at felipe.bogaerts@engenharia.ufjf.br.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from apps.mainsite import views

urlpatterns = [
    path("", views.home, name="home"),
    path("aboutme/", views.aboutme, name="aboutme"),
    path("wood/", views.wood, name="wood"),
    path("admin/", admin.site.urls, name="admin"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
