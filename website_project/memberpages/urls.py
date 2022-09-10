from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.memberpages.as_view(), name='memberpages'),
    path('memberpages/', views.logankeim.as_view(), name='logankeim'),
]

