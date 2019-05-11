from django.db import models

# Create your models here.
class Package(models.Model):
    package_id = models.CharField(max_length=30, null=True)
    package_name = models.CharField(max_length=30, null=True)
    company_name = models.CharField(max_length=30, null=True)
    package_cc = models.CharField(max_length=60)
    package_type = models.CharField(max_length=60, null=True)
    price = models.FloatField()
    detail = models.CharField(max_length=200, null=True)
    active = models.IntegerField(default=1)

    def __str__(self):
        return 'ID: ' + str(self.id) + ' ,' + self.package_name+ ' ,' + self.company_name

class Promotion(models.Model):
    promotion_name = models.CharField(max_length=30)
    promotion_detail = models.CharField(max_length=200)
    end_date = models.DateField(null=True)

    def __str__(self):
        return str(self.id) + self.promotion_name