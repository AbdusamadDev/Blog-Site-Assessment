from django.urls import path

from .views import BlogsDetailView, BlogsCreateView


urlpatterns = [
    path("details/<int:pk>", BlogsDetailView.as_view(), name="blogs-detail"),
    path("create/", BlogsCreateView.as_view(), name="blogs-create"),
]
