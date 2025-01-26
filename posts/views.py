from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from authors.models import Author


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.views += 1
    post.save()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        img = request.FILES.get('img')
        content = request.POST.get('comment')
        author, created = Author.objects.get_or_create(first_name=first_name, last_name=last_name)
        Comment.objects.create(
            post=post,
            author=author,
            content=content
        )
        return redirect('posts:detail', post_id=post.id)
    return render(request, 'posts/post-detail.html', {'post': post})
