from django.urls import path

from .views import CustomLoginView, logout_view, RegistrationView


urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout-user/", logout_view, name="logout"),
]
