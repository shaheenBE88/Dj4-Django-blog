from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class PostCreate(CreateView):
    model = Post
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = reverse_lazy('post_list')

class PostUpdate(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    form_class = PostForm
    success_url = reverse_lazy('post_list')

class PostDelete(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post_list')