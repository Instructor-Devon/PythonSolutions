from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000 -> views.index()
    path("", views.index),
    path("login", views.login),
    path("register", views.register),
    path("success", views.success)
]