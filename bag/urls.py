from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("add_to_bag", views.add_to_bag, name="add_to_bag"),
]