from django import forms
from django.shortcuts import get_object_or_404
from django.forms import DateTimeField
from .models import Insure
from package_control.models import Package
from customer.models import Car, Customer

pack_choice = lambda: [(pack.package_id, pack.package_name) for pack in Package.objects.order_by('id')]
car_choice = lambda: [(car.id, car.car_number) for car in Car.objects.order_by('id')]
cus_choice = lambda: [(cus.id, cus.fname) for cus in Customer.objects.order_by('id')]

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

class NewCusForm(forms.Form):
    doc_nbr = forms.CharField(max_length=30, label="รหัสกรมธรรม์")
    package_id = forms.ChoiceField(choices=pack_choice, label="เลือกแพ็คเกจ", widget=forms.Select(
        attrs={'class': 'selectpicker', 'data-live-search': 'true'}))
    company_order = forms.CharField(max_length=30, label="บริษัทประกัน")
    price = forms.FloatField(label="ราคาสุทธิ")
    total_price = forms.FloatField(label="ราคารวม")
    post_date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}
    ), label="วันที่(ด/ว/ป)")

class TranferForm(forms.Form):
    pic_balance = forms.ImageField()