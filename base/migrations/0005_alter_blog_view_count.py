# Generated by Django 5.0.3 on 2024-03-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_blog_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='view_count',
            field=models.BigIntegerField(default=0),
        ),
    ]