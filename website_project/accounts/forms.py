from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from .models import UserProfile


# Make sure this class is not the same name as "UserCreationForm"
class UserCreateForm(UserCreationForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        email_source = email.split('@')[-1]
        permitted_sources = ['live.esu.edu', 'esu.edu']

        if email_source not in permitted_sources:
            raise ValidationError("That is not a valid email address.")

        return email

    class Meta:
        # the fields I want the user to be able to access when they are signing up
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.is_active = False
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'ESU Email Address'


class LoginForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                try:
                    user_temp = User.objects.get(username=username)
                except:
                    user_temp = None

                if user_temp is not None and user_temp.check_password(password):
                    self.confirm_login_allowed(user_temp)
                else:
                    raise forms.ValidationError(
                        self.error_messages['invalid_login'],
                        code='invalid_login',
                        params={'username': self.username_field.verbose_name},
                    )

        return self.cleaned_data


class UserEditUser(ModelForm):    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

class UserEditProfile(ModelForm):
    class meta:
        model = UserProfile
        fields = ('dob', 'bio')