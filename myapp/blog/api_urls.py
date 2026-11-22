from django.urls import path
from .api_views import PostListAPIView, PostDetailAPIView, CategoryListAPIView, CategoryDetailAPIView
app_name = "api"

urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name="post-list"),
    path("posts/<slug:slug>/", PostDetailAPIView.as_view(), name="post-detail"),
    path("categories/",  CategoryListAPIView.as_view(), name="category-list",),
    path("categories/<int:pk>/", CategoryDetailAPIView.as_view(), name="category-detail",)
]
