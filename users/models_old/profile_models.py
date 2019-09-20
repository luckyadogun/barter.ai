# import uuid

# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
# from django.utils.text import slugify

# from django_countries.fields import CountryField
# from taggit.managers import TaggableManager

# from users.managers import CustomUserManager
# from users.choices import (ACCOUNT_TYPE_CHOICES, 
#     ACCOMPLISHMENT_TYPE, ACCOMPLISHMENT_STATUS_CHOICES as ASC,
#     LANGUAGE_CHOICES, TIMEZONE)


# class User(AbstractUser):
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
#     #TODO: check if exists
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     mobile = models.CharField(max_length=100, blank=True, null=True)
#     location = CountryField()
#     language = models.CharField(max_length=200, choices=LANGUAGE_CHOICES)
#     timezone = models.CharField(max_length=200, choices=TIMEZONE)
#     email_notif_on = models.BooleanField(default=False)
#     skills = TaggableManager()
#     date_of_birth = models.DateField()
#     # url = models.SlugField(unique=True) # needed

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def get_full_name(self):
#         f'{self.fist_name} {self.last_name}' # TODO: check this

#     def __str__(self):
#         return self.get_full_name()

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.url = slugify(f'{self.first_name} {self.last_name} {str(uuid.uuid4()[:7])}')


#entrep cant access the feeds page
#enteps cant comment on a pitch
#can ONLY view implementers who like or connect with their pitch
#premium: cant have 30 connects for startups they want to invest on: why wait to run out?

#implementers cant create/edit/delete pitch
#cant view other implementers on a pitch
#premium: can see a list of implementers with the skillsets needed/location and chat them up: why wait?

#users should be able to move from one account type to another but could lose access to permission

#display industry trends on dashboard
#display account trends
#display supporters

# class Entrepreneur(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # account_type = models.CharField(max_length=200, choices=ACCOUNT_TYPE_CHOICES)
#     startup_name = models.CharField(max_length=200, blank=True, null=True)

#     #TODO: set permissions
    
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'



#entrep cant access the feeds page
#enteps cant comment on a pitch
#can ONLY view implementers who like or connect with their pitch
#premium: cant have 30 connects for startups they want to invest on: why wait to run out?

#implementers cant create/edit/delete pitch
#cant view other implementers on a pitch
#premium: can see a list of implementers with the skillsets needed/location and chat them up: why wait?

#users should be able to move from one account type to another but could lose access to permission

#display industry trends on dashboard
#display account trends
#display supporters
    

# class Education(models.Model):
#     college = models.CharField(max_length=200)
#     degree = models.CharField(max_length=200)
#     field_of_study = models.CharField(max_length=200)
#     start_year = models.DateField()
#     end_year = models.DateField()
#     grade = models.CharField(max_length=200, blank=True, null=True)
#     activities_or_societies = models.CharField(max_length=200)
#     description = models.TextField()
#     media = models.FileField(upload_to='CV')
#     media_url = models.URLField()
#     link = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return f'{self.college}'


# class License(models.Model):
#     name = models.CharField(max_length=200, blank=False, null=False)
#     issuer = models.CharField(max_length=200, blank=False, null=False)
#     issue_date = models.DateField(null=True)
#     expiry_date = models.DateField(null=True)
#     credential_id = models.CharField(max_length=200, null=False, blank=False)
#     credential_url = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return f'{self.name}'

    

# class Education(models.Model):
#     college = models.CharField(max_length=200)
#     degree = models.CharField(max_length=200)
#     field_of_study = models.CharField(max_length=200)
#     start_year = models.DateField()
#     end_year = models.DateField()
#     grade = models.CharField(max_length=200, blank=True, null=True)
#     activities_or_societies = models.CharField(max_length=200)
#     description = models.TextField()
#     media = models.FileField(upload_to='CV')
#     media_url = models.URLField()
#     link = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return f'{self.college}'


# class License(models.Model):
#     name = models.CharField(max_length=200, blank=False, null=False)
#     issuer = models.CharField(max_length=200, blank=False, null=False)
#     issue_date = models.DateField(null=True)
#     expiry_date = models.DateField(null=True)
#     credential_id = models.CharField(max_length=200, null=False, blank=False)
#     credential_url = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return f'{self.name}'


# class Accomplishment(models.Model):
#     title = models.CharField(max_length=200, blank=False, null=False)
#     acc_type = models.CharField(max_length=200, choices=ACCOMPLISHMENT_TYPE)
#     acc_status = models.CharField(max_length=200, choices=ASC)
#     start_year = models.DateField()
#     end_year = models.DateField()
#     description = models.TextField()
#     link = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return f'{self.title}'


# class Implementer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     education = models.ForeignKey(Education, on_delete=models.CASCADE, null=True, blank=True)
#     license = models.ForeignKey(License, on_delete=models.CASCADE, null=True, blank=True)
#     accomplishnment = models.ForeignKey(Accomplishment, on_delete=models.CASCADE, null=True, blank=True)
#     connects = models.IntegerField(default=10)

#     def __str__(self):
#         return f'{self.user}'


    
