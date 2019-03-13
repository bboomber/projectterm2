from django import forms
from .models import Package

CAR_TYPE = (
    ('','Choose...'),
    ('รถเก๋ง', 'รถเก๋ง'),
    ('รถกระบะ', 'รถกระบะ')
)

class PackageForm(forms.Form):
    package_id = forms.CharField(max_length=30, label="รหัสแพ็คเกจ")
    package_name = forms.CharField(max_length=30, label="ชื่อแพ็คเกจ")
    compamy_name = forms.CharField(max_length=30, label="ชื่อบริษัท")
    package_cc = forms.IntegerField(label="ซีซี")
    package_type  = forms.ChoiceField(choices=CAR_TYPE)
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