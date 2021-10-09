from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.ProjectPage.as_view(), name='projects'),
    path('extra-life/', views.ExtraLifePage.as_view(), name='extralife'),
    path('telescope/', views.TelescopePage.as_view(), name ='telescope'),
    path('conferences/', views.ConferencesPage.as_view(), name='conferences'),
    path('windturbine/', views.WindTurbinePage.as_view(), name='windturbine'),
    path('gamedev/', views.GameDevPage.as_view(), name='gamedev'),
]