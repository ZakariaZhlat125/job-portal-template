from django.db import models
from Accounts.models import User


class Company (models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    description =models.TextField(max_length=1500)


    def __str__(self):
        return self.name
    