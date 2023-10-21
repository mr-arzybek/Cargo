from django.contrib.auth import hashers
from rest_framework import status, response
from rest_framework.response import Response
from django.utils import timezone
from api.users import models
from .email import send_email_reset_password
from .models import User
from .token import recovery_code


class ResetPasswordSendEmail:

    @staticmethod
    def password_reset_email(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            email = serializer.validated_data["email"]
            user = models.User.objects.get(email=email)
        except:
            return response.Response(
                data={"error": "Пользователь с указанным адресом электронной почты не найден."},
                status=status.HTTP_404_NOT_FOUND)
        time = timezone.now() + timezone.timedelta(minutes=5)
        password_reset_token = models.PasswordResetToken(
            user=user, code=recovery_code, time=time)
        password_reset_token.save()
        send_email_reset_password(user.email)
        return response.Response(data={"detail": f'код для сброса пароля отправлен на вашу почту {user.email}'},
                                 status=status.HTTP_200_OK)


class PasswordResetCode:
    @staticmethod
    def password_reset_code(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            code = serializer.validated_data["code"]
            reset_code = models.PasswordResetToken.objects.get(
                code=code, time__gt=timezone.now()
            )
        except Exception as e:
            return response.Response(
                status=status.HTTP_406_NOT_ACCEPTABLE,
                data={
                    "error": f"Недействительный код для сброса пароля или время истечения кода закончилось.{e}"},
            )
        return response.Response(
            data={"detail": "success", "code": f"{code}"}, status=status.HTTP_200_OK)


class PasswordResetNewPassword:
    @staticmethod
    def password_reset_new_password(code, password):
        try:
            password_reset_token = models.PasswordResetToken.objects.get(
                code=recovery_code, time__gt=timezone.now()
            )
        except models.PasswordResetToken.DoesNotExist:
            return False, "Недействительный код для сброса пароля или время истечения кода закончилось."

        user = password_reset_token.user
        user.password = hashers.make_password(password)
        user.save()

        password_reset_token.delete()
        return True, "Пароль успешно обновлен"
