from core.models import Post, Tag
from django.shortcuts import render


def blog_view(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    return render(request, "blog/blog.html", {"posts": posts, "tags": tags})
