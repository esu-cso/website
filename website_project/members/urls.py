from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.MembersPage.as_view(), name='members'),
    path('PMaute/', views.PMautePaige.as_view(), name='PMaute'),
]