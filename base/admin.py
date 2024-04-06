from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "status"]
    actions = None  # Disable bulk actions

    def get_queryset(self, request):
        queryset = super().get_queryset(request).exclude(status="approved")
        return queryset.order_by("status")


admin.site.register(Blog, BlogAdmin)
