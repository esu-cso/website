from django.contrib import admin

# Register your models here.
from django.apps import AppConfig
from django.contrib import admin
from accounts.models import UserProfile


admin.site.register(UserProfile)
