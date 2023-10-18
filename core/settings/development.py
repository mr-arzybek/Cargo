
from decouple import config

from core.settings.base import BASE_DIR

SECRET_KEY = config("SECRET_KEY")

# DEBUG = config('DEBUG')
DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://localhost",
    "http://127.0.0.1:",
    "http://localhost:8080",
    "http://127.0.0.1",
    "https://4f8c-109-201-175-115.ngrok-free.app"
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = [
    "https://4f8c-109-201-175-115.ngrok-free.app"
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:88" "http://web:8080",
    "http://web:80",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080",

]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://127.0.0.1:8000'
    'https://4f8c-109-201-175-115.ngrok-free.app'
]

CORS_ALLOW_HEADERS = (
    'content-disposition', 'accept-encoding',
    'content-type', 'accept', 'origin', 'Authorization', 'access-control-allow-methods',
    'Access-Control-Allow-Origin'
)

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
