# coding: utf-8

from django.shortcuts import render

from django.views.generic import (
    View
)

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from app.core.models import (
    Blog
)


class ViewBlog(View):

    template_name = 'view.html'

    def get(self, request, blog_id):

        blog = Blog.objects.get(id=blog_id)

        return render(
            request,
            self.template_name,
            {
                'blog': blog
            }
        )



class AddBlog(View):

    template_name = 'add.html'

    def get(self, request):


        return render(
            request,
            self.template_name,
            {

            }
        )


    def post(self, request):

        title = request.POST.get('title')
        content = request.POST.get('content')

        blog = Blog(
            title=title,
            content=content
        )
        blog.save()

        return HttpResponse('add blog success!!!')


