from rest_framework import serializers
from django.contrib.auth import authenticate

class PasswordResetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        style={"input_type": "password"}, help_text="From 6 to 20", min_length=6
    )


class PasswordResetCodeSerializer(serializers.Serializer):
    code = serializers.CharField()


class PasswordResetSearchUserSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ['email']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        # Проверяем соответствие логина и пароля
        user = authenticate(username=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        else:
            raise serializers.ValidationError("Invalid email or password.")