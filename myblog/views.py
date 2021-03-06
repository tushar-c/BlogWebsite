from django.shortcuts import render
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myblog/index.html', {'posts': posts})


def about(request):
    return render(request, 'myblog/about.html')


def home(request):
    return render(request, 'myblog/blog.html')


def post_view(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'myblog/post_view.html', {'post':post})
