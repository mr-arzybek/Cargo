from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserCustomManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password):
        user = self.model(
        email = self.normalize_email(email),
                password = password,)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        self.create_user(email,password )
        self.user.is_staff()
        self.user.is_superuser = True
        self.user.save()
        return self.user

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    password = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password_reset_code = models.CharField(max_length=6, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserCustomManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class PasswordResetToken(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    time = models.DateTimeField()

