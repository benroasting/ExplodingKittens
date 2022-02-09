from django.shortcuts import render
from django.views import View
from .models import Post, Comment
from .forms import PostForm, CommentForm

class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'feed/post_list.html', context)

class CreatePostView(View):
    def get(self, request, *args, **kwargs):
        form = PostForm()

        context = {
            'form': form,
        }

        return render(request, 'feed/create_post.html', context)

    def post(self, request, *args, **kwargs): 
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST, request.FILES)   

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'feed/post_list.html', context)

class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'feed/post_comment.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save() 

        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'feed/post_comment.html', context)