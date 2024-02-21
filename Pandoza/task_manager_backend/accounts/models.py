from django.db import models
from django.contrib.auth.models import UserManager, Group, Permission, AbstractUser


class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class Accounts(AbstractUser):
    role = models.CharField(max_length=150, null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    class Meta:
        db_table = 'accounts'

    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)


class Employees(models.Model):
    employee = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True, blank=True, related_name='employee')
    employee_name = models.CharField(max_length=150, null=True, blank=True)
    
    class Meta:
        db_table = 'employees'
