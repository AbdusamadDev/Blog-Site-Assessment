from django.views.generic import DetailView

from .models import Blog

class BlogsDetailView(DetailView):
    model = Blog
    template_name = "test.html"
