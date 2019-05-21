from django import forms
from .models import Package, Promotion
from django.forms import DateTimeField

class PackageForm(forms.Form):
    package_id = forms.CharField(max_length=30, label="รหัสแพ็คเกจ")
    package_name = forms.CharField(max_length=30, label="ชื่อแพ็คเกจ")
    compamy_name = forms.CharField(max_length=30, label="ชื่อบริษัท")
    package_cc = forms.CharField(label="ซีซี")
    package_type = forms.CharField(max_length=30, label="ประเภทแพ็คเกจ")
    price = forms.FloatField(label="ราคา")
    detail = forms.CharField(max_length=200, label="รายละเอียด")

    class Meta:
        model = Package
        fields = ('package_id',
                  'package_name',
                  'company_name',
                  'package_cc',
                  'package_type',
                  'price',
                  'detail',
                  )


class PromotionForm(forms.Form):
    promotion_name = forms.CharField(max_length=30, label="ชื่อโปรโมชั่น")
    promotion_detail = forms.CharField(max_length=200, label="รายละเอียด")
    end_date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}
    ), label="วันที่(ด/ว/ป)")

    class Meta:
        model=Promotion
        fields=('promotion_name',
        'promotopn_detial',
        'edt_date')
