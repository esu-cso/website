from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required, permission_required


app_name = 'accounts'

urlpatterns = [
    path('', views.MembersPage.as_view(), name='memberspage'),
    path('login/', views.LogInPage.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpPage.as_view(), name='signup'),
    path('profile/', views.ProfilePage.as_view(), name='profile'),
]
