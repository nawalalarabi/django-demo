from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from rest_framework import generics

from . import serializers
from .models import Post
from .forms import PostForm, PostEdit


def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


class AddPost(View):
    template_name = 'add_post.html'
    form_class = PostForm()

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        self.form_class = PostForm(request.POST)
        if self.form_class.is_valid():
            post = self.form_class.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')

        return render(request, self.template_name, {'form': self.form_class})


class PostShow(View):
    template_name = 'post_show.html'

    def get(self, request, year=None, month=None, slug=None):
        user = request.user
        post = get_object_or_404(Post, slug=slug)

        return render(request, self.template_name, {'member': user,
                                             'post': post})


class PostEditView(View):
    form_class = None
    template_name = 'post_edit.html'

    def get(self, request, year=None, month=None, slug=None):
        post = get_object_or_404(Post, slug=slug)

        self.form_class = PostEdit(initial={
            'title': post.title,
            'content': post.content
        })

        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, year=None, month=None, slug=None):
        self.form_class = PostEdit(request.POST)
        post = get_object_or_404(Post, slug=slug)
        post_date = post.pub_date

        if self.form_class.is_valid():
            cleaned_data = self.form_class.cleaned_data
            post.title = cleaned_data['title']
            post.content = cleaned_data['content']
            post.save(update_fields=['title', 'content'])
            return redirect(post.get_absolute_url())

        return render(request, self.template_name, {'form': self.form_class})


class PostDelete(View):
    template_name = 'post_delete.html'

    def get(self, request, year=None, month=None, slug=None):
        post = get_object_or_404(Post, slug=slug)
        return render(request, self.template_name, {'post': post})

    def post(self, request, year=None, month=None, slug=None):
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return redirect('home')


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostAddAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostShowAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostEditAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

