from django.urls import path

from .views import (
    RegistrationView,
    CustomLoginView,
    DashboardView,
    logout_view,
)


urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout-user/", logout_view, name="logout"),
    path("dashboard/<int:pk>/", DashboardView.as_view(), name="dashboard"),
]
