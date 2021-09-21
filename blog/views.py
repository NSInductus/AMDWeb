from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    queryset = Post.objects.filter(public = True)
    paginate_by = 3

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post.html"
    
class CategoryListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    paginate_by = 3
    def get_queryset(self):
        return Post.objects.filter(public = True).filter(categories__in = Category.objects.filter(id = self.kwargs['pk']))