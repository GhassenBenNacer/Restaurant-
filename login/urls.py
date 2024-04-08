from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import update_profile , update_password


urlpatterns = [

path('login/', views.login_user ,name='login'),
path('logout/', views.logout_user, name='logout' ),
path('change-password/', auth_views.PasswordChangeView.as_view(template_name="change-password.html"), name='change-password'),
path('modifier-profile/',update_profile , name='updateProfil'),
path('modifier-MDP/',update_password , name='updatePassword')

]
