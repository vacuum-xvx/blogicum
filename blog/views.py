from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Post, Category

app_name = 'blog'

def index(request):
    template = 'blog/index.html'
    posts = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]

    context = {'posts': posts}
    return render(request, template, context)

def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        id=id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )
    context = {'post': post}
    return render(request, template, context)

def category_posts(request, category_slug):
    template = 'blog/category.html'

    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')

    context = {
        'category': category,
        'post_list': post_list,
    }

    return render(request, template, context)