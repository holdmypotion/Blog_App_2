from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
        ).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}

    return render(request, 'blog/post_list.html', stuff_for_frontend)

def detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = {'post': post}

    return render(request, 'blog/post_detail.html', stuff_for_frontend)

def post_edit_view(request, pk=None):
    post = Post.objects.filter(pk=pk).first()
    if request.method == 'POST':
        if post:
            form = PostForm(request.POST, instance=post)
        else:
            form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)

    else:
        if post:
            form = PostForm(instance=post)
        else:
            form = PostForm()
        stuff_for_frontend = {'form': form}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)
