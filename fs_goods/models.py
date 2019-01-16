# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField


class GoodsType(models.Model):
    gtitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)


class GoodsInfo(models.Model):
    gname = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='fs_goods')
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    gunit = models.CharField(max_length=20)
    gclick = models.IntegerField()
    gjianjie = models.CharField(max_length=200)
    gkucun = models.IntegerField()
    gcontent = HTMLField()
    gtype = models.ForeignKey(GoodsType)
    # gadv = models.BooleanField(default=False)
    idDelete = models.BooleanField(default=False)

