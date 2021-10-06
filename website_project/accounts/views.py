from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
class SignUpPage(CreateView):
    form_class = forms.UserCreateForm
    # reverse lazy to wait for them to click sign up first
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class LogInPage(LoginView):
    template_name = 'accounts/login.html'

class MembersPage(TemplateView):
     template_name = 'accounts/members.html'

class ProfilePage(TemplateView):
    template_name = 'accounts/profile.html'
