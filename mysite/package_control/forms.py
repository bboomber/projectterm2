from django import forms
from .models import Package, Promotion
from django.forms import DateTimeField

com_choice = (
    ("A ประกันภัย", ("A ประกันภัย")),
    ("B ประกันภัย", ("B ประกันภัย")),
    ("C ประกันภัย", ("C ประกันภัย")),
    ("D ประกันภัย", ("D ประกันภัย")),
    ("E ประกันภัย", ("E ประกันภัย")),
    ("F ประกันภัย", ("F ประกันภัย")),
    ("G ประกันภัย", ("G ประกันภัย")),
    ("H ประกันภัย", ("H ประกันภัย")),
    ("I ประกันภัย", ("I ประกันภัย")),
    ("J ประกันภัย", ("J ประกันภัย")),
    ("K ประกันภัย", ("K ประกันภัย")),
    ("L ประกันภัย", ("L ประกันภัย")),
    ("M ประกันภัย", ("M ประกันภัย")),
    ("N ประกันภัย", ("N ประกันภัย")),
    ("O ประกันภัย", ("O ประกันภัย")),
    ("P ประกันภัย", ("P ประกันภัย")),
    ("Q ประกันภัย", ("Q ประกันภัย")),
)
pack_choice = lambda: [(pack.package_id, pack.package_name) for pack in Package.objects.filter(active=2).order_by('id')]

class PackageForm(forms.Form):
    package_id = forms.CharField(max_length=30, label="รหัสแพ็คเกจ")
    package_name = forms.CharField(max_length=30, label="ชื่อแพ็คเกจ")
    company_name = forms.ChoiceField(choices=com_choice, label="บริษัท", widget=forms.Select(
        attrs={'class': 'selectpicker' , 'data-live-search': 'true'}))
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
