from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

from base.views import BlogsListView

urlpatterns = (
    [
        path("accounts/", include("authentication.urls")),
        path("comments/", include("comments.urls")),
        path("", BlogsListView.as_view(), name="home"),
        path("base/", include("base.urls")),
        path("admin/", admin.site.urls),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
