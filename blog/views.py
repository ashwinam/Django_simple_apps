from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post

# Create your views here.

def createPost(request):
    form = PostForm
    context = {'form':form ,'Heading': 'Post'}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            mark1 = form.save(commit = False)
            mark1.author = request.user
            form.save()
            return redirect('allpost')

    return render (request, 'blog/post.html', context)


def allpost(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'blog/allpost.html', context)
