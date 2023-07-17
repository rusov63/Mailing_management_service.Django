from django.core.management import BaseCommand
from users.models import User
from dotenv import load_dotenv
import os


PASSWORD = os.getenv('Pass_SQL') # введите пароль
EMAIL_USER = os.getenv('@'), # укажите почту для входа в админ панель

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email= EMAIL_USER,
            first_name='Admin',
            last_name='SuperUser',
            is_staff=True,
            is_superuser=True
        )

        user.set_password(PASSWORD)
        user.save()
