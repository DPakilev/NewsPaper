from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    template_name = "news.html"
    context_object_name = 'news'
    ordering = ['-data_time']
    paginate_by = 10


class PostSearchView(ListView):
    model = Post
    template_name = "search_news.html"
    context_object_name = 'news'
    ordering = ['-data_time']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostCreateView(CreateView):
    template_name = 'add_news.html'
    form_class = PostForm


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()


class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


class PostUpdateView(UpdateView):
    template_name = 'add_news.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
