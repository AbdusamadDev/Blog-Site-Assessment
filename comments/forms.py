from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    parent_comment = forms.IntegerField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ["text"]
