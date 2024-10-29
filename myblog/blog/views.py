from django.http import Http404
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Post not found.")

    return render(request, 'blog/post/detail.html', {'post': post})


