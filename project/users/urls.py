from django.urls import path
from django.contrib.auth.forms import PasswordChangeForm
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]