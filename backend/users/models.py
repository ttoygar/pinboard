from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import BaseModel

class CustomUser(AbstractUser, BaseModel):
    
    email = models.EmailField(_("email address"), blank=True, unique=True)
