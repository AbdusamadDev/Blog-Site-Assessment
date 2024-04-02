from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    next_page = reverse_lazy("home")