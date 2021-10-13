from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required, permission_required


app_name = 'accounts'

urlpatterns = [
    path('', login_required(views.MembersPage.as_view()), name='memberspage'),
    path('profile/', login_required(views.ProfilePage.as_view()), name='profile'),
    path('login/', views.LogInPage.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpPage.as_view(), name='signup'),    
    path('signedup/', views.SignedUpPage.as_view(), name='signedup')
]
