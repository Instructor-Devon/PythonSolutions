from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('message/create', views.create_message),
    path('comment/create', views.create_comment),
]