from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer
from .email import EmailAuthentication
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, response
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


class LoginView(APIView):
    authentication_classes = [EmailAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                token = RefreshToken.for_user(user)
                access_token = token.access_token
                return Response({"access": str(token) ,'refresh': str(access_token)}, status=status.HTTP_200_OK)
            return Response({"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)