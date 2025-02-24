from django.shortcuts import render
from django.http import Http404


posts_dict = {item['id']: item for item in posts}


def index(request):
    context = {'posts': posts[::-1]}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    try:
        context = {'post': posts_dict[post_id]}
    except KeyError:
        raise Http404(f"Пост с ID - {post_id} не найден")
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    context = {'category_slug': category_slug}
    return render(request, 'blog/category.html', context)
