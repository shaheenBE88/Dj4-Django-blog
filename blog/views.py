from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    data = Post.objects.all()
    return render(request, 'post_list.html', {'posts': data})

def post_detail(request, post_id):
    data = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'posts': data})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)  # Bind form data
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('post_list')  # Redirect to the post list
    else:
        form = PostForm()  # Create an empty form for GET requests
    
    return render(request, 'new_post.html', {'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    
    return render(request, 'delete_post.html', {'post': post})