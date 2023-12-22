from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator


def all_posts(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'all_posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})
