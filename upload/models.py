# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', blank = False, null = True, default = None)
    title = models.CharField(max_length=200)
    file = models.FileField(null=True)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(
            default=timezone.now)

    def upload(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



