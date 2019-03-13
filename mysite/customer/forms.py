from django import forms
from .models import Car, Customer

class CustomerForm(forms.Form):
    cus_id = forms.CharField(max_length=30, label="รหัสลูกค้า")
    fname = forms.CharField(max_length=30, label="ชื่อ")
    lname = forms.CharField(max_length=30, label="นามสกุล")
    address = forms.CharField(max_length=200, label="ที่อยู่")
    province = forms.CharField(max_length=30, label="จังหวัด")
    zipcode = forms.CharField(max_length=5, label="รหัสไปรษณีย์")
    id_card = forms.CharField(max_length=13, label="เลขบัตรประชาชน")
    phone = forms.CharField(max_length=15, label="เบอร์โทรศัพท์")
    email = forms.EmailField()

    class Meta:
        model = Customer
        fields = ('cus_id',
        'fname',
        'lname',
        'address',
        'province',
        'zipcode',
        'id_card',
        'phone',
        'email',
        )

class CarForm(forms.Form):
    car_id = forms.CharField(max_length=30, label="รหัสรถยนต์")
    car_number = forms.CharField(max_length=30, label="ทะเบียนรถ")
    province = forms.CharField(max_length=30, label="จังหวัดทะเบียน")
    brand = forms.CharField(max_length=30, label="ยี่ห้อรถ")
    chassis_number = forms.CharField(max_length=30, label="เลขตัวถัง")
    model = forms.CharField(max_length=30, label="รุ่นรถยนต์")
    car_cc = forms.IntegerField(label="ซีซี")
    car_type = forms.CharField(max_length=30, label="ประเภทรถยนต์")
    sit = forms.IntegerField(label="ที่นั่ง")
    
    class Meta:
        model = Car
        fields = ('car_id',
        'car_number',
        'province',
        'brand',
        'chassis_number',
        'model',
        'car_cc',
        'car_type',
        'sit',
        )