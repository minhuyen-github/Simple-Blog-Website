from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    context = { 'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

posts = [
    {
        'author': 'someOne',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'someOneEh',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 27, 2019'
    }
]
