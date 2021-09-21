from django.urls import path
from .views import BlogListView, BlogDetailView, CategoryListView

blog_patterns = ([
    path('', BlogListView.as_view(), name="post_list"),
    path('<int:pk>/', BlogDetailView.as_view(), name="post_detail"),
    path('category/<int:pk>/', CategoryListView.as_view(), name="post_list_category"),
], 'blog')