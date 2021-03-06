# coding: utf-8
from django.conf.urls import patterns, url
from app.csrf.views import (
    AddBlog,
    ViewBlog
)

urlpatterns = patterns(
    '',
    url(
        r'^add/$',
        AddBlog.as_view(),
        name='blog-csrf-add',
    ),
    url(
        r'^view/(?P<blog_id>\d+)/$$',
        ViewBlog.as_view(),
        name='blog-csrf-view',
    ),

)