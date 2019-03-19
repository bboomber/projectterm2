from django import forms
from django.shortcuts import get_object_or_404
from django.forms import DateTimeField
from .models import Insure
from package_control.models import Package
from customer.models import Car, Customer

pack_list = Package.objects.order_by('id')
pack_choice = []
for pack in pack_list:
    pack_choice.append((pack.package_id, pack.package_name))

car_list = Car.objects.order_by('id')
car_choice = []
for car in car_list:
    car_choice.append((car.id, car.car_number))

cus_list = Customer.objects.order_by('id')
cus_choice = []
for cus in cus_list:
    cus_choice.append((cus.id, cus.fname))


class InsureForm(forms.Form):
    doc_nbr = forms.CharField(max_length=30, label="รหัสกรมธรรม์")
    package_id = forms.ChoiceField(choices=pack_choice, label="เลือกแพ็คเกจ", widget=forms.Select(
        attrs={'class': 'selectpicker', 'data-live-search': 'true'}))
    cus_id = forms.ChoiceField(choices=cus_choice, label="เลือกลูกค้า", widget=forms.Select(
        attrs={'class': 'selectpicker', 'data-live-search': 'true'}))
    car_id = forms.ChoiceField(choices=car_choice, label="เลือกรถยนต์", widget=forms.Select(
        attrs={'class': 'selectpicker', 'data-live-search': 'true'}))
    company_order = forms.CharField(max_length=30, label="บริษัทประกัน")
    price = forms.FloatField(label="ราคาสุทธิ")
    total_price = forms.FloatField(label="ราคารวม")
    post_date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}
    ), label="วันที่(ด/ว/ป)")

    class Meta:
        model = Insure
        fields = ('doc_nbr',
                  'package_id',
                  'car_id',
                  'cus_id',
                  'car_number',
                  'company_order',
                  'price',
                  'total_price',
                  'post_date',
                  )
