from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here


class HomeView(TemplateView):
    template_name = 'home.html'


class ListPage(ListView):
    model = Post

    template_name = 'list_page.html'


class DetailPage(DetailView):
    model = Post

    template_name = 'object_page.html'

class NewPostPage(CreateView):
    template_name = 'new_post.html'
    model = Post
    fields = ['title','author','body']


class UpdatePost(UpdateView):
    template_name = 'update_post.html'
    model = Post
    fields = ['title','author','body']


class DeletePost(DeleteView):
    template_name = 'delete_post.html'
    model = Post
    success_url = reverse_lazy('home') 
