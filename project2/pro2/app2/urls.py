from django.contrib import admin
from django.urls import include, path
from app2 import views

urlpatterns = [
    path('', views.users, name='users'),
]
