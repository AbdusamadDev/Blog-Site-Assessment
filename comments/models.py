from django.db import models
from ckeditor.fields import RichTextField


class Comment(models.Model):
    user = models.ForeignKey("authentication.Account", on_delete=models.CASCADE)
    text = RichTextField(max_length=2000)
    blog = models.ForeignKey(to="base.Blog", on_delete=models.CASCADE, default=1)
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"

    def get_descendants(self):
        descendants = []
        for reply in self.replies.all():
            descendants.append(reply)
            descendants.extend(reply.get_descendants())
        return descendants
