from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from eduser.managers import UserManager
import uuid


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    firstname = models.CharField(max_length=100, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    lastname = models.CharField(max_length=100, blank=False, null=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    def __str__(self):
        return self.email