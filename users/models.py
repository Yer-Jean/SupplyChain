from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings


class User(AbstractUser):
    username = None  # удаляем поле username, так как авторизовать будем по полю email
    email = models.EmailField(unique=True, verbose_name='Email')

    first_name = models.CharField(max_length=50, verbose_name='Name', **settings.NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name='Surname', **settings.NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Phone number', **settings.NULLABLE)
    city = models.CharField(max_length=50, verbose_name='City', **settings.NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('email',)

    def __str__(self):
        return self.email
