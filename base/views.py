from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    CreateView,
    ListView,
)


from .forms import BlogsForm
from .models import Blog


class BlogsDetailView(DetailView):
    model = Blog
    template_name = "blog-detail.html"


class BlogsCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "blog-create.html"
    form_class = BlogsForm
    success_url = reverse_lazy("home")


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_list_view = BlogsListView()
        blog_list_view.setup(self.request)
        queryset = blog_list_view.get_queryset()
        context["object_list"] = queryset
        paginator = blog_list_view.get_paginator(queryset, blog_list_view.paginate_by)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context["page_obj"] = page_obj
        context["is_paginated"] = page_obj.has_other_pages()
        return context


class BlogsListView(ListView):
    template_name = "blog-list.html"
    paginate_by = 8
    model = Blog



