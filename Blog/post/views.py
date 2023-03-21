from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.views.generic.edit import DeleteView, UpdateView


# Create your views here.


def hello(request):
    return HttpResponse("My name is Dean")


def greet(request):
    return HttpResponse("Welcome to Django class")


def welcome(request):
    posts = Post.objects.all()
    return render(request, 'post/welcome.html', {'posts': posts})


def comment(request):
    posts1 = Post.objects.all()
    return render(request, 'post/comment.html', {'posts': posts1})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'


class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post/post_new.html'
    fields = ['title', 'body', 'author',]
    success_url = reverse_lazy('home')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('home')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/post_edit.html'
    fields = ['title', 'body']
