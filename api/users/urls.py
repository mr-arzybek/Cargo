from django.urls import path
from django.contrib.auth import views as auth_views

from api.users import views
from api.users.views import PasswordResetRequestAPIView, PasswordResetCodeAPIView, PasswordResetNewPasswordAPIView, \
    LoginView

urlpatterns = [
    path("reset-password-email/", PasswordResetRequestAPIView.as_view(), name="search user and send mail"),
    path("reset-password-code/", PasswordResetCodeAPIView.as_view(), name="write code"),
    path("reset-new-password/<str:code>/", PasswordResetNewPasswordAPIView.as_view(), name="write new password"),
    path('login/', LoginView.as_view(), name='login'),
]
