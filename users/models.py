from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import  BaseUserManager, AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail

# ATTENTION! 
# Below 'CustomUserManager' and 'User' classes are used to override default Django user logic.
# It may be confusing, please don't worry if You don't understand it :)   
# Regards, Prem

# class CustomUserManager(BaseUserManager):
#     """
#     Custom user model manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """
#     def create_user(self, email, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not email:
#             raise ValueError(_('The Email must be set'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('type', 0)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
#         return self.create_user(email, password, **extra_fields)


# class User(AbstractBaseUser, PermissionsMixin):
#     """
#     A class implementing a fully featured User model with
#     admin-compliant permissions.

#     Email and password are required. Other fields are optional.
#     """
    
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=17, blank=True, unique=True)
#     first_name = models.CharField(max_length=50, blank=False, null=False)
#     last_name = models.CharField(max_length=50, blank=False, null=False)

#     is_staff = models.BooleanField(
#         _('staff status'),
#         default=False,
#         help_text=_('Designates whether the user can log into this admin site.'),
#     )

#     is_active = models.BooleanField(
#         _('active'),
#         default=True,
#         help_text=_(
#             'Designates whether this user should be treated as active. '
#             'Unselect this instead of deleting accounts.'
#         ),
#     )
    
#     date_joined = models.DateTimeField(default=timezone.now)

#     objects = CustomUserManager()

#     EMAIL_FIELD = 'email'
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
    
#     def __str__(self):
#         return self.email
    
#     def clean(self):
#         super().clean()
#         self.email = self.__class__.objects.normalize_email(self.email)

#     def email_user(self, subject, message, from_email=None, **kwargs):
#         """Send an email to this user."""
#         send_mail(subject, message, from_email, [self.email], **kwargs)

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(max_length=17, blank=True, unique=True)

    def __str__(self):
        return self.name
    

class Driver(models.Model):
    phone_number = models.CharField(max_length=17, blank=True, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    car_model = models.CharField(max_length=50, blank=False, null=False)
    car_color = models.CharField(max_length=50, blank=False, null=False)
    car_license_plate = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.first_name +" "+ self.last_name
    

