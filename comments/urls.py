from django.urls import path

from .views import blog_detail


urlpatterns = [
    path("create/<int:blog_id>/", blog_detail, name="comment"),
]
