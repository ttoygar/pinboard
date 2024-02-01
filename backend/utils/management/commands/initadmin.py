from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time
from core.settings import ADMIN_NAME, ADMIN_PASS
from users.models import CustomUser as User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if User.objects.count() == 0:
            if not ADMIN_NAME or not ADMIN_PASS:
                print("Admin info can not be found")
            else:
                username = ADMIN_NAME
                email = ""
                password = ADMIN_PASS
                print("Creating admin account")
                admin = User.objects.create_superuser(email=email, username=username, password=password)
                admin.is_active = True
                admin.is_admin = True
                admin.save()
                print("Admin account is created")
        else:
            print("Admin user can only be created if no admin exists.")

