from django.shortcuts import render, redirect

from app.forms import PostForm
from app.models import Post


# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context=context)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.image = form.cleaned_data['image']
            post.save()
            return redirect('index')
    context = {'form': PostForm()}
    return render(request, 'add.html', context=context)


def details(request, post_id):
    post = Post.objects.filter(id=post_id).get()
    context = {'post': post}
    return render(request, 'details.html', context=context)
