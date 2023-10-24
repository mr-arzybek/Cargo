from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
import random
import secrets

User = get_user_model()




confirmation_code = random.randint(1000, 9999)
recovery_code = secrets.token_urlsafe(4)

