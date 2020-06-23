from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('clicks/get', views.get_clicks),
    path('clicks/set', views.set_clicks),
]