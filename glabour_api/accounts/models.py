from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")

class CustomAccountManager(BaseUserManager):
    def create_user(self,email,first_name,password,**other_fields):
        if not email:
            raise ValueError(_('Please provide an email address'))
        email=self.normalize_email(email)
        user=self.model(email=email,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,first_name,password,**other_fields):
        other_fields.setdefault('is_labour',True)
        other_fields.setdefault('is_admin',True)
        other_fields.setdefault('is_active',True)
        return self.create_user(email,first_name,password,**other_fields)


class Accounts(AbstractBaseUser):
    email=models.EmailField(unique=True)
    phone = models.CharField(max_length=200, validators=[phone_validator], unique=False)
    first_name = models.CharField(_('first_name'),max_length=150)
    last_name = models.CharField(_('last_name'),max_length=150)
    is_active=models.BooleanField(default=True)
    is_labour = models.BooleanField()
    is_admin = models.BooleanField(default=False)
    new_user_status = models.BooleanField(default=True,null=True,blank=True)
    
    objects= CustomAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['email',"phone",'first_name']

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'Accounts'
