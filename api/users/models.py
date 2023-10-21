from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserCustomManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, ):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    password = models.CharField(max_length=20)
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

