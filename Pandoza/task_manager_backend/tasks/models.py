from django.db import models
from accounts.models import Accounts

class Tasks(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    task = models.CharField(max_length=225, null=True)
    status = models.CharField(max_length=150, null=True)

    class Meta:
        db_table = 'tasks'