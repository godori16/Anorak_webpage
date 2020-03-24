from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    company_name = models.TextField()
