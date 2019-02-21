from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    agent_code = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    id_card = models.CharField(max_length=13)
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=200)
    remark = models.CharField(max_length=200)
    
    def __str__(self):
        return self.agent_code

@receiver(post_save, sender=User)
def update_Employee(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
    instance.employee.save()