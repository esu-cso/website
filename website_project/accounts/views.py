from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, UpdateView
#from .models import UserProfile
from accounts.forms import (UserCreateForm, UserEditUser, UserEditProfile)
from django.contrib.auth import update_session_auth_hash


# Create your views here.
class SignUpPage(CreateView):
    form_class = UserCreateForm
    # reverse lazy to wait for them to click sign up first
    success_url = reverse_lazy('accounts:signedup')
    template_name = 'accounts/signup.html'

class LogInPage(LoginView):
    template_name = 'accounts/login.html'

class MembersPage(TemplateView):
     template_name = 'accounts/members.html'

class ProfilePage(UpdateView):   
    form_class = UserEditUser
    template_name = 'accounts/profile.html'
        

class SignedUpPage(TemplateView):
    template_name = 'accounts/signedup.html'

