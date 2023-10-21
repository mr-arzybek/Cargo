from django.contrib.auth import logout

from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, response
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import (
    PasswordResetSearchUserSerializer, PasswordResetCodeSerializer, PasswordResetNewPasswordSerializer)


from .service import ResetPasswordSendEmail, PasswordResetCode, PasswordResetNewPassword

class PasswordResetRequestAPIView(generics.CreateAPIView):
    serializer_class = PasswordResetSearchUserSerializer


    def post(self, request, *args, **kwargs):
        reset_password_service = ResetPasswordSendEmail()
        return reset_password_service.password_reset_email(self, request)


class PasswordResetCodeAPIView(generics.CreateAPIView):
    serializer_class = PasswordResetCodeSerializer


    def post(self, request, *args, **kwargs):
        reset_password_code = PasswordResetCode()
        return reset_password_code.password_reset_code(self, request)


class PasswordResetNewPasswordAPIView(generics.CreateAPIView):
    serializer_class = PasswordResetNewPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            code = kwargs["code"]
            password = serializer.validated_data["password"]
            success, message = PasswordResetNewPassword.password_reset_new_password(code, password)
            if success:
                return response.Response(data={"detail": message}, status=status.HTTP_200_OK)
            else:
                return response.Response(data={"detail": message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
