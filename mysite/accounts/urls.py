from accounts import views
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path("login/", views.MyLoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("about-me/", views.AboutMeView.as_view(), name="about-me"),
    path("logout/", views.MyLogoutView.as_view(), name="logout"),
]
