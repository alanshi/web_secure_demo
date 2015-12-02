# coding: utf-8

from django.shortcuts import render
from collections import namedtuple
from django.db import connection
from django.views.generic import (
    View
)

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from app.core.models import (
    Blog
)


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

class ViewBlog(View):

    template_name = 'view.html'

    def get(self, request):

        blog_id = request.GET.get('blog_id')
        cursor = connection.cursor()

        sql = "SELECT title,content FROM core_blog WHERE id = '%s';" % blog_id

        print sql

        cursor.execute(sql)
        blog = namedtuplefetchall(cursor)
        if blog:
            blog = blog[0]

        return render(
            request,
            self.template_name,
            {
                'blog': blog
            }
        )


