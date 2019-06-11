from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.Field(label="ชื่อlogin", widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.PasswordInput()
    password2 = forms.Field(label="พาสเวิร์ด2", widget=forms.TextInput(attrs={'class':'form-control'}))
    fname = forms.CharField(max_length=30, label="ชื่อ")
    lname = forms.CharField(max_length=30, label="นามสกุล")
    id_card = forms.CharField(max_length=13, label="เลขบัตรประชาชน")
    phone1 = forms.CharField(max_length=15, label="เบอร์โทรศัพท์1")
    phone2 = forms.CharField(max_length=15, label="เบอร์โทรศัพท์2")
    email = forms.EmailField(label="อีเมลล์")
    address = forms.CharField(max_length=200, label="ที่อยู่")
    class Meta:
        model = User
        fields = ('username',
                  'password1',
                  'password2',
                  'fname',
                  'lname',
                  'id_card',
                  'phone1',
                  'phone2',
                  'email',
                  'address',
                  )


class EditProfileForm(UserCreationForm):
    fname = forms.CharField(max_length=30)
    lname = forms.CharField(max_length=30)
    id_card = forms.CharField(max_length=13)
    phone1 = forms.CharField(max_length=15)
    phone2 = forms.CharField(max_length=15)
    email = forms.EmailField()
    address = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('fname',
                  'lname',
                  'id_card',
                  'phone1',
                  'phone2',
                  'email',
                  'address',
                  )
