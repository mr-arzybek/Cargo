from django.core.mail import send_mail

from .models import User
from .token import confirmation_code, recovery_code
from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth import get_user_model


def send_email_reset_password(email):
    subject = "Восстановление пароля"
    message = f"Код для восстановления пароля: <<< {recovery_code} >>> Код действителен в течении 5 минут"
    email_from = 'dreeemanndreemann@gmail.com'
    send_mail(subject, message, email_from, [email])


class EmailAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        email = request.data.get('email')  # Предполагается, что email передается в теле запроса
        password = request.data.get('password')

        if not email or not password:
            return None

        User = get_user_model()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        if user.check_password(password):
            return (user, None)

        raise exceptions.AuthenticationFailed('No such user')
