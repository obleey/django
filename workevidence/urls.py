from django.urls import path
from . import views


urlpatterns = [
    path('', views.default, name='landing'),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout")

]