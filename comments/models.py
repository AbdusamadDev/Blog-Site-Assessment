from ckeditor.fields import RichTextField
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey("authentication.Account", on_delete=models.CASCADE)
    text = RichTextField(max_length=2000)
    blog = models.ForeignKey(to="base.Blog", on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"

