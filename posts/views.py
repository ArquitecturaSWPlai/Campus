
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    
class Home(TemplateView):
    template_name = "home.html"
