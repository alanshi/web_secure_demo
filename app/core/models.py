# coding: utf-8

from django.db import models


class Blog(models.Model):

    title = models.CharField(
        max_length=50,
        verbose_name='标题'
    )
    content = models.TextField(
        verbose_name='内容'
    )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = verbose_name
