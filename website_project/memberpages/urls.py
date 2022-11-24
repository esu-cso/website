from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.memberpages.as_view(), name='memberpages'),
    path('logankeim/', views.logankeim.as_view(), name='logankeim'),
    path('johnwinward/', views.johnwinward.as_view(), name='johnwinward'),
    path('williamyouse/', views.williamyouse.as_view(), name='williamyouse'),
    path('gabrielquadrino/', views.gabrielquadrino.as_view(), name='gabrielquadrino'),
    path('roshanforde/', views.roshanforde.as_view(), name='roshanforde'),
    path('benchernin/', views.benchernin.as_view(), name='benchernin')
]

