from django.conf.urls import url
from django.urls import path, re_path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name='account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ]
