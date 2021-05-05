from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reminder(models.Model):
    company_name = models.CharField(max_length=50)
    expire_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)