from django.urls import path

from .views import (
    BlogsDetailView,
    BlogsCreateView,
    hit_like_to_blog,
    v2_template_view,
    BlogsListView,
)


urlpatterns = [
    path("details/<int:pk>", BlogsDetailView.as_view(), name="blogs-detail"),
    path("create/", BlogsCreateView.as_view(), name="blogs-create"),
    path("blogs", BlogsListView.as_view(), name="blogs-list"),
    path("like/<int:pk>", hit_like_to_blog, name="like"),
    path("v2/", v2_template_view, name="v2"),
]
