import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from django_countries.fields import CountryField
from taggit.managers import TaggableManager

from users.models import User
from utils.choices import ACCOMPLISHMENT_TYPE, OFFER_STATUS_CHOICES




# class Messages(models.Model):
#     sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     receiver = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     body = models.TextField()
#     created_at = models.DateField(auto_now_add=True)

#     def __str__(self):
#         f'{self.body[:30]} at {self.created_at}'



class Portfolio(models.Model):

    title = models.CharField(max_length=200, blank=False, null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d')

    def __str__(self):
        return f'{self.title}'


class Accomplishment(models.Model):

    title = models.CharField(max_length=200, blank=False, null=False)
    acc_type = models.CharField(max_length=200, choices=ACCOMPLISHMENT_TYPE)

    def __str__(self):
        return f'{self.title}'

        
class Entrepreneur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    location = CountryField(blank=True, null=True)
    email_notif_on = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, null=True)
    skills = TaggableManager(blank=True)
    date_joined = models.DateField(auto_now_add=True)
    accomplishnment = models.ForeignKey(Accomplishment, on_delete=models.CASCADE, null=True, blank=True)
    portfolio = models.ManyToManyField(Portfolio, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    url = models.SlugField(unique=True)    

    def __str__(self):
        return f'{self.user}'

    def save(self, *args, **kwargs):
        self.url = slugify(f'{self.user.first_name} {self.user.last_name} {self.user.id}')
        super(Entrepreneur, self).save(*args, **kwargs)


class Pitch(models.Model):
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    skills = models.CharField(max_length=200, blank=True)
    offer_status = models.CharField(max_length=20, choices=OFFER_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

