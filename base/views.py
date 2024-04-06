from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.db.models.base import Model as Model
from django.forms import BaseModelForm
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    CreateView,
    ListView,
)

from datetime import datetime

from .forms import BlogsForm
from .models import Blog


class BlogsDetailView(DetailView):
    model = Blog
    template_name = "blog-detail.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        response = super().get(request, *args, **kwargs)
        blog = self.get_object()
        current_time = datetime.now()
        date_incremented = blog.increment_date
        till_when = current_time.timestamp() - date_incremented
        if till_when > 120:  # 120 = 2(60 seconds) -> 2 minutes
            blog.view_count += 1
            blog.increment_date = current_time.timestamp()
            blog.save()
        return response


class BlogsCreateView(LoginRequiredMixin, CreateView):
    template_name = "blog-create.html"
    form_class = BlogsForm
    success_url = reverse_lazy("home")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


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


class BlogsListView(LoginRequiredMixin, ListView):
    template_name = "blog-list.html"
    paginate_by = 8
    model = Blog
    queryset = (
        Blog.objects.all().filter(status="approved").order_by("-date_created")
    )  # First return all approved-by-admin blogs and return the latest news


@login_required
def hit_like_to_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.like_count += 1
    blog.save()
    return HttpResponse(str(pk))
