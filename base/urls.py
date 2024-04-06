from django.urls import path

from .views import BlogsDetailView, BlogsCreateView, BlogsListView, hit_like_to_blog


urlpatterns = [
    path("details/<int:pk>", BlogsDetailView.as_view(), name="blogs-detail"),
    path("create/", BlogsCreateView.as_view(), name="blogs-create"),
    path("blogs", BlogsListView.as_view(), name="blogs-list"),
    path("like/<int:pk>", hit_like_to_blog, name="like"),
]
