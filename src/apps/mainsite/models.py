# -*- coding: utf-8 -*-
# Author: Felipe Bogaerts de Mattos
# Contact me at felipe.bogaerts@engenharia.ufjf.br.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.

from django.db import models


class Bow(models.Model):
    instrument_choices = [
        ("VI", "Violin"),
        ("VO", "Viola"),
        ("CE", "Cello"),
        ("DB", "Double Bass"),
    ]
    sound_choices = [
        ("Bright", "bright"),
        ("Dark", "dark"),
    ]
    shape_choices = [
        ("Octagonal", "octagonal"),
        ("Round", "round"),
    ]
    shade_choices = [
        ("Light Brown", "light_brown"),
    ]

    name = models.CharField(max_length=255)
    instrument = models.CharField(
        max_length=30, choices=instrument_choices, default="VI"
    )
    description = models.TextField(max_length=1000)
    text = models.TextField(max_length=10000, blank=True)

    # Information:
    weight = models.FloatField(blank=True, null=True)
    sound = models.CharField(blank=True, null=True, choices=sound_choices)
    shape = models.CharField(blank=True, null=True, choices=shape_choices)
    shade = models.CharField(blank=True, null=True, choices=shade_choices)

    tip = models.ImageField(upload_to="mainsite/media/")
    frog = models.ImageField(upload_to="mainsite/media/")

    def __str__(self):
        return self.title
