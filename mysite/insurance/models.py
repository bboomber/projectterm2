from django.db import models
from employee_control.models import Employee
from customer.models import Customer, Car
from package_control.models import Package

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Insure(models.Model):
    doc_nbr = models.CharField(max_length=30, null=True)
    agent_code = models.ForeignKey(Employee, on_delete=models.CASCADE)
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    cus_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    car_number = models.CharField(max_length=15, null=True)
    company_order = models.CharField(max_length=30, null=True)
    price = models.FloatField()
    total_price = models.FloatField()
    post_date = models.DateField(null=True)
    confirm = models.IntegerField(default=2)

    def __str__(self):
        return str(self.id)


class Tranfer(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Package_id = models.ForeignKey(Package, on_delete=models.CASCADE)
    balance = models.FloatField()
    pic_balance = models.ImageField(upload_to='pic_balance')