from django import forms
from django.shortcuts import get_object_or_404
from django.forms import DateTimeField
from .models import Insure
from package_control.models import Package


class InsureForm(forms.Form):
    pack_list = Package.objects.order_by('id')
    pack_choice = []
    for pack in pack_list:
        pack_choice.append((pack.package_id, pack.package_name))

    doc_nbr = forms.CharField(max_length=30, label="รหัสกรมธรรม์")
    package_id = forms.ChoiceField(choices=pack_choice, label="เลือกแพ็คเกจ")
    car_id = forms.CharField(max_length=30, label="รหัสรถยนต์")
    cus_id = forms.CharField(max_length=30, label="รหัสลูกค้า")
    car_number = forms.CharField(max_length=30, label="ทะเบียนรถ")
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
