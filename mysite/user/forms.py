from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    agent_code = forms.CharField(max_length=30)
    fname = forms.CharField(max_length=30)
    lname = forms.CharField(max_length=30)
    id_card = forms.CharField(max_length=13)
    phone1 = forms.CharField(max_length=15)
    phone2 = forms.CharField(max_length=15)
    email = forms.EmailField()
    address = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('username',
        'password1',
        'password2',
        'agent_code',
        'fname',
        'lname',
        'id_card',
        'phone1',
        'phone2',
        'email',
        'address',
        )
