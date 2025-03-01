from django.shortcuts import get_object_or_404, render

from .models import Post, Category
from .constants import MAX_POSTS_ON_PAGE


def index(request):
    return render(request, 'blog/index.html',
                  {'post_list': Post
                   .filter_published()
                   .order_by('pub_date')[:MAX_POSTS_ON_PAGE]})


def post_detail(request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html',
                  {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True,)
    return render(request, 'blog/index.html',
                  {'post_list': Post
                   .filter_published()
                   .filter(category=category)
                   .order_by('pub_date')})
