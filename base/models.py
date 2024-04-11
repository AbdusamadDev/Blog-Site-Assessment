from ckeditor.fields import RichTextField
from django.db import models

from authentication.models import Account


class Blog(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    )
    title = models.CharField(max_length=100)
    user = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    document = models.FileField(upload_to="docs/")
    body = RichTextField(max_length=7000)
    view_count = models.BigIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    increment_date = models.BigIntegerField(default=1)
    like_count = models.BigIntegerField(default=0)



