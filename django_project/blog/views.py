from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context=context)

class PostListView(ListView):
    model = Post
    # Template name by default appname/modelname_viewtype.html => blog/post_list.html
    template_name = 'blog/home.html'

    # Contect_object_name by default post_list then we have to override it.
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    # for the template we wouldn't chang it as we are going to use the default name.
    context_object_name = 'post'


def about(request):
    return render(request, 'blog/about.html', {'title':'About'},)