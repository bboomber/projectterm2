from django import forms
from django.shortcuts import get_object_or_404
from django.forms import DateTimeField
from .models import Insure
from package_control.models import Package
from customer.models import Car, Customer

pack_choice = lambda: [(pack.package_id, pack.package_name) for pack in Package.objects.filter(active=2).order_by('id')]
car_choice = lambda: [(car.id, car.car_number) for car in Car.objects.order_by('id')]
cus_choice = lambda: [(cus.id, cus.fname) for cus in Customer.objects.order_by('id')]

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

class InsureForm(forms.Form):
    doc_nbr = forms.CharField(max_length=30, label="รหัสกรมธรรม์")
    package_id = forms.ChoiceField(choices=pack_choice, label="เลือกแพ็คเกจ", widget=forms.Select(
        attrs={'class': 'selectpicker', 'data-live-search': 'true'}))
    cus_id = forms.ChoiceField(choices=cus_choice, label="เลือกลูกค้า", widget=forms.Select(
        attrs={'class': 'selectpicker', 'data-live-search': 'true'}))
    car_id = forms.ChoiceField(choices=car_choice, label="เลือกรถยนต์", widget=forms.Select(
        attrs={'class': 'selectpicker', 'data-live-search': 'true'}))
    company_order = forms.ChoiceField(choices=com_choice, label="เลือกรถยนต์", widget=forms.Select(
        attrs={'class': 'selectpicker', 'data-live-search': 'true'}))
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
class InsureEditForm(InsureForm):
    doc_nbr = forms.CharField(max_length=30, label="รหัสกรมธรรม์")
    package_id = forms.CharField()
    cus_id = forms.CharField()
    car_id = forms.CharField()
    company_order = forms.ChoiceField(choices=com_choice, label="บริษัท", widget=forms.Select(
        attrs={'class': 'selectpicker' , 'data-live-search': 'true'}))
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

class SellingForm(forms.Form):
    cus_fname = forms.CharField(max_length=30, label="ชื่อ")
    cus_lname = forms.CharField(max_length=30, label="นามสกุล")
    cus_address = forms.CharField(max_length=200, label="ที่อยู่")
    cus_province = forms.CharField(max_length=30, label="จังหวัด")
    cus_zipcode = forms.CharField(max_length=5, label="รหัสไปรษณีย์")
    cus_id_card = forms.CharField(max_length=13, label="เลขบัตรประชาชน")
    cus_phone = forms.CharField(max_length=15, label="เบอร์โทรศัพท์")
    cus_email = forms.EmailField(label="อีเมลล์")
    # -------------
    car_number = forms.CharField(max_length=30, label="ทะเบียนรถ")
    car_province = forms.CharField(max_length=30, label="จังหวัดทะเบียน")
    car_brand = forms.CharField(max_length=30, label="ยี่ห้อรถ")
    car_chassis_number = forms.CharField(max_length=30, label="เลขตัวถัง")
    car_model = forms.CharField(max_length=30, label="รุ่นรถยนต์")
    car_cc = forms.CharField(label="ซีซี")
    car_type = forms.CharField(max_length=30, label="ประเภทรถยนต์")
    car_sit = forms.IntegerField(label="ที่นั่ง")
    # ------------------
    package_id = forms.ChoiceField(choices=pack_choice, label="เลือกแพ็คเกจ", widget=forms.Select(
        attrs={'class': 'selectpicker', 'data-live-search': 'true'}))
    # ------------------
    pic_balance = forms.ImageField()
