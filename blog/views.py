from django.shortcuts import render, get_object_or_404
from . models import Post


def blog_posts(request):
    posts = Post.objects.order_by('-created_at').filter(active = True)
    context = {
        'posts':posts
    }
    return render(request, 'blog/blog-posts.html', context)


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post':post,
    }
    return render(request, 'blog/post-details.html', context)