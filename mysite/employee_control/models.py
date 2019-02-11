from django.db import models

# Create your models here.
class Employee(models.Model):
    agent_code = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    id_card = models.CharField(max_length=13)
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=200)
    remark = models.CharField(max_length=200)