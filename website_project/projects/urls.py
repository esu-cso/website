from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings


urlpatterns = [
    path('projects/', views.ProjectPage.as_view(), name='projects'),
    path('extra-life/', views.ExtraLife.as_view(), name='extralife'),

]