# Generated by Django 5.0.3 on 2024-04-02 18:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_blog_status_delete_pendingblogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(max_length=7000),
        ),
    ]