from django.urls import path

from .views import BlogsDetailView

urlpatterns = [
    path("test/<int:pk>", BlogsDetailView.as_view(), name="blogs-detail"),
]
