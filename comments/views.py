from django.shortcuts import render, get_object_or_404, redirect

from .models import Comment
from .forms import CommentForm
from base.models import Blog


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = Comment.objects.filter(
        blog__id=blog_id, parent_comment=None
    )  # Adjusted to use blog__id
    previous_page = redirect(request.META.get("HTTP_REFERER", "/"))
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            parent_comment_id = form.cleaned_data.get("parent_comment")
            parent_comment = None
            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
            Comment.objects.create(
                user=request.user,
                text=form.cleaned_data["text"],
                blog=blog,  # This assumes you have a ForeignKey named `blog` in your Comment model
                parent_comment=parent_comment,
            )
            return previous_page

    return render(
        request, "comment.html", {"blog": blog, "comments": comments, "form": form}
    )
