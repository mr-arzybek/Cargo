from django.core.mail import send_mail

from .models import User
from .token import confirmation_code, recovery_code

def send_email_reset_password(email):
    subject = "Восстановление пароля"
    message = f"Код для восстановления пароля: <<< {recovery_code} >>> Код действителен в течении 5 минут"
    email_from = 'dreeemanndreemann@gmail.com'
    send_mail(subject, message, email_from, [email])

