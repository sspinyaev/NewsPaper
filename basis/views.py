from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
from datetime import datetime


class PostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_auto_now_add_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_time'] = datetime.utcoffset()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'
