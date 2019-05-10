from django import forms

class Empform(forms.Form):
    agent_code = forms.CharField(label="agent_code", max_length=30)
    fname = forms.CharField(label="fname", max_length=30)
    lname = forms.CharField(label="lname", max_length=30)
    id_card = forms.CharField(label="id_card", max_length=13)
    phone1 = forms.CharField(label="phone1", max_length=15)
    phone2 = forms.CharField(label="phone2", max_length=30)
    email = forms.CharField(label="email", max_length=30)
    address = forms.CharField(label="address", max_length=200)