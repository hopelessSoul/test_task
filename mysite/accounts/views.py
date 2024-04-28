from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from accounts.models import Profile


class AboutMeView(TemplateView):
    template_name = "accounts/about-me.html"


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:about-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


class MyLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        return reverse_lazy("accounts:about-me")


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")
