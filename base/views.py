from django.views.generic import DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
 

from .forms import BlogsForm
from .models import Blog


class BlogsDetailView(DetailView):
    model = Blog
    template_name = "blog-detail.html"


class BlogsCreateView(CreateView):
    model = Blog
    template_name = "blog-create.html"
    form_class = BlogsForm
    success_url = reverse_lazy("home")

class HomeView(TemplateView):
    template_name = "home.html"
    