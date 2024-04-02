from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render


class RegistrationView(FormView):
    template_name = "auth/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    next_page = reverse_lazy("home")


def logout_view(request):
    if not request.user.is_authenticated:
        return HttpResponse(reverse_lazy("login"))

    logout(request)
    return render(template_name="auth/logged_out.html", request=request, context={})
