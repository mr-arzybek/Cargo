from rest_framework import serializers


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
