import random

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


def login_user(serializer):
    user = authenticate(
        email=serializer.validated_data["email"],
        password=serializer.validated_data["password"]
    )

    if user:
        refresh = RefreshToken.for_user(user=user)
        access_token = str(refresh.access_token)
        response = {'access': access_token, 'refresh': str(refresh)}
        return Response(data=response, status=status.HTTP_200_OK)
    else:
        return Response(
            data={"message": "Invalid email or password"},
        )


def generate_random_code():
    code = random.randint(100000, 999999)
    return code
