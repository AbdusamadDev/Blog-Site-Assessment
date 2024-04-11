from django import forms

from .models import Blog


class BlogsForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "document", "body"]

