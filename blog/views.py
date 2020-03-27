from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog_new.html'
    fields = ['title', 'thumbnail_image', 'thumbnail_text', 'body']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'thumbnail_image', 'thumbnail_text', 'body']
    template_name = 'blog_edit.html'
    login_url = 'login'

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog')
    login_url = 'login'