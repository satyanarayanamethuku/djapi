from django.db import models

# Create your models here.


class Hyderabad(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=256)
    title=models.CharField(max_length=256)
    eligibility=models.CharField(max_length=256)
    address=models.CharField(max_length=256)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=20)