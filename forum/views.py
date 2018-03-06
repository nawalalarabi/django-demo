from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Post
from .forms import PostForm


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
    template_name = 'post_show'

    def get(self, request, year, month, slug):
        user = request.user
        post = get_object_or_404(Post, slug=slug)

        render(request, self.template_name, {'member': user,
                                             'post': post})
