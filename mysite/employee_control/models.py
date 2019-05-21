from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # agent_code = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    id_card = models.CharField(max_length=13)
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=30, null=True)
    address = models.CharField(max_length=200)
    remark = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=30, default='broker')
    zipcode = models.CharField(max_length=5, null=True)
    sub_district = models.CharField(max_length=30, null=True)
    distinct = models.CharField(max_length=30, null=True)
    province = models.CharField(max_length=30, null=True)
    

    def __str__(self):
        return 'ID: ' + str(self.id) + ' ,' + self.fname
    
    class Meta:
        permissions = [
            ("is_admin", "Role is admin"),
            ("is_manager", "Role is manager"),
        ]

@receiver(post_save, sender=User)
def update_Employee(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
    instance.employee.save()





