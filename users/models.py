from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from users.managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.get_full_name()


class PasswordRecovery(models.Model):
    secret = models.CharField(max_length=100, unique=True)
    expires = models.DateField(auto_now_add=True) #same day
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


