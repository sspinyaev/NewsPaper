from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .filters import PostFilter
from .forms import PostForm
from .models import Post


class PostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_auto_now_add_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_time'] = datetime.utcoffset()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'


class PostSearch(ListView):
    form_class = PostFilter
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(CreateView, PermissionRequiredMixin):
    permission_required = ('basis.add_news',)
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.CATEGORY_CHOISES = 'NW'
        return super().form_valid(form)


class NewsEdit(UpdateView, PermissionRequiredMixin):
    permission_required = ('basis.update_news',)
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.CATEGORY_CHOISES = 'NW'
        return super().form_valid(form)


class NewsDelete(DeleteView, PermissionRequiredMixin):
    permission_required = ('basis.delete_news',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('/news/')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.CATEGORY_CHOISES = 'NW'
        return super().form_valid(form)


class ArticleCreate(CreateView, PermissionRequiredMixin):
    permission_required = ('basis.add_article',)
    form_class = PostForm
    model = Post
    template_name = 'aricle_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.CATEGORY_CHOISES = 'AR'
        return super().form_valid(form)


class ArticleEdit(UpdateView, PermissionRequiredMixin):
    permission_required = ('basis.update_article',)
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.CATEGORY_CHOISES = 'AR'
        return super().form_valid(form)


class ArticleDelete(DeleteView, PermissionRequiredMixin):
    permission_required = ('basis.delete_article',)
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('/news/')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.CATEGORY_CHOISES = 'NW'
        return super().form_valid(form)



