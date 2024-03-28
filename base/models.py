from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=1)
    document = models.FileField(upload_to="docs/")
    body = RichTextField(max_length=6000, default="...")
    view_count = models.BigIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
