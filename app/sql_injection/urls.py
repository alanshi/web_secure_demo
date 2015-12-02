# coding: utf-8
from django.conf.urls import patterns, url
from app.sql_injection.views import (
    ViewBlog
)

urlpatterns = patterns(
    '',
    url(
        r'^view/$',
        ViewBlog.as_view(),
        name='blog-sql-view',
    ),

)