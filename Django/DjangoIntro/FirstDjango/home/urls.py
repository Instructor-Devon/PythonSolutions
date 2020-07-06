from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/
    path('', views.index),
    # localhost:8000/new
    path('new', views.new),
    # localhost:8000/create
    path('create', views.create),
    # localhost:8000/1
    # localhost:8000/100
    path('<int:number>', views.show),
    path('<int:number>/edit', views.edit),
    path('<int:number>/delete', views.destroy)
]