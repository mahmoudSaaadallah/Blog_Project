from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'Mahmoud',
        'title': 'Blog Post 1',
        'content' : 'first post content',
        'date_posted' : 'August 27, 2018'
    },
    {
        'author': 'Omar',
        'title': 'Blog Post 2',
        'content' : 'second post content',
        'date_posted' : 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'},)