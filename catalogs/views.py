from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q  # Q obyekti kerak bo'ladi
from posts.models import Post
from tags.models import Tag
from catalogs.models import Catalog


def home(request):
    category_filter = request.GET.getlist('category')
    sort_by = request.GET.get('sort', 'latest')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    hashtag_filter = request.GET.getlist('hashtag')
    query = request.GET.get('q')
    posts = Post.objects.all()
    tags = Tag.objects.all()
    catalogs = Catalog.objects.all()
    if category_filter:
        try:
            category_filter = [int(c) for c in category_filter]
            posts = posts.filter(catalog__id__in=category_filter)
        except ValueError:
            posts = posts.none()
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    if hashtag_filter:
        posts = posts.filter(tags__id__in=hashtag_filter)
    if start_date and end_date:
        posts = posts.filter(created_at__range=[start_date, end_date])
    if sort_by == 'latest':
        posts = posts.order_by('-created_at')
    elif sort_by == 'oldest':
        posts = posts.order_by('created_at')
    elif sort_by == 'popular':
        posts = posts.order_by('-views')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {
        'page_obj': page_obj,
        'category_filter': category_filter,
        'tags': tags,
        'catalogs': catalogs,
    })
