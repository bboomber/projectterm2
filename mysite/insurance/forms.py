from django import forms
from django.forms import DateTimeField
from .models import Insure


class InsureForm(forms.Form):
    doc_nbr = forms.CharField(max_length=30, label="รหัสกรมธรรม์")
    package_id = forms.CharField(max_length=30, label="รหัสแพ็คเกจ")
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