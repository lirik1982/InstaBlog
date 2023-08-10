from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib import messages
from .forms import PostCreateForm, PostEditForm


def home_view(request):
    posts = Post.objects.all()

    return render(request, "posts/home.html", {'posts': posts})


def post_create_view(request):
    form = PostCreateForm()
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'posts/create.html', {'form': form})


def post_delete_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted')
        return redirect('home')

    return render(request, 'posts/delete.html', {'post': post})


def post_edit_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = PostEditForm(instance=post)

    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            messages.success(request, 'Post updated')
            return redirect('home')

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'posts/edit.html', context)


def post_page_view(request, pk):
    post = get_object_or_404(Post, id=pk)

    return render(request, 'posts/post_page.html', {'post': post})
