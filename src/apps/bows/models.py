# -*- coding: utf-8 -*-
# Author: Felipe Bogaerts de Mattos
# Contact me at felipe.bogaerts@engenharia.ufjf.br.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.

from django.db import models


class MyBow(models.Model):
    instruments = [
        ("VI", "Violin"),
        ("VO", "Viola"),
        ("CE", "Cello"),
        ("DB", "Double Bass"),
    ]
    title = models.CharField(max_length=100)
    instrument = models.CharField(
        max_length=30, choices=instruments, default="VI"
    )
    description = models.CharField(max_length=250)
    text = models.TextField(max_length=2000, blank=True)
    tip = models.ImageField(upload_to="mainsite/media/")
    frog = models.ImageField(upload_to="mainsite/media/")

    def __str__(self):
        return self.title
