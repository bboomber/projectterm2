from django.db import models

# Create your models here.

class Customer(models.Model):
    cus_id = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=200, null=True)
    province = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=5)
    id_card = models.CharField(max_length=13)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    cus_type = models.IntegerField(default=1)

    def __str__(self):
        return 'ID: ' + str(self.id)

class Car(models.Model):
    car_id = models.CharField(max_length=30)
    car_number = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    chassis_number = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    car_cc = models.IntegerField()
    car_type = models.CharField(max_length=30)
    sit = models.IntegerField()

    def __str__(self):
        return 'ID: ' + str(self.id)