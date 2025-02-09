from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

# Create your views here


class HomeView(TemplateView):
    template_name = 'home.html'


class ListPage(ListView):
    model = Post

    template_name = 'list_page.html'


class DetailPage(DetailView):
    model = Post

    template_name = 'object_page.html'
