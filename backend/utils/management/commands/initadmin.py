from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if User.objects.count() == 0:
            username = "a"
            email = ""
            password = "1"
            print("Creating admin account")
            admin = User.objects.create_superuser(email=email, username=username, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print("Admin user can only be created if no admin exists.")

