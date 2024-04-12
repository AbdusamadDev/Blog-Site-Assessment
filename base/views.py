from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.db.models.base import Model as Model
from django.core.paginator import Paginator
from django.forms import BaseModelForm
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    CreateView,
    ListView,
)

from datetime import datetime
from typing import Any

from comments.models import Comment
from .forms import BlogsForm
from .models import Blog


class BlogsDetailView(DetailView):
    model = Blog
    template_name = "blog-detail.html"
    paginate_by = 10  # Number of comments per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()
        comments = Comment.objects.filter(blog=blog, parent_comment=None).order_by(
            "-created_at"
        )  # Fetch top-level comments related to the blog and order them by created_at
        paginator = Paginator(comments, self.paginate_by)
        page_number = self.request.GET.get(
            "page"
        )  # Get the current page number from the request query parameters
        page_obj = paginator.get_page(page_number)
        context["comments"] = page_obj  # Add the paginated comments to the context

        return context

    def get(self, request, *args, **kwargs):
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
    paginate_by = 3
    model = Blog
    queryset = (
        Blog.objects.all().filter(status="approved").order_by("-date_created")
    )  # First return all approved-by-admin blogs and return the latest blogs


@login_required
def hit_like_to_blog(request, pk):
    user = request.user
    blog = get_object_or_404(Blog, pk=pk)
    previous_page = redirect(request.META.get("HTTP_REFERER", "/"))

    # Check if the user hadn't already liked the target blog
    if user.liked_blogs.filter(pk=pk).exists():
        return previous_page

    # Proceed with liking the blog
    blog.like_count += 1
    blog.save()
    user.liked_blogs.add(blog)

    # Redirect back to the previous page
    return previous_page
