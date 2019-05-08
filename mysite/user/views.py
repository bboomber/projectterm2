from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from employee_control.models import Employee
from django.http import HttpResponse


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.employee.fname = form.cleaned_data.get('fname')
            user.employee.lname = form.cleaned_data.get('lname')
            user.employee.id_card = form.cleaned_data.get('id_card')
            user.employee.phone1 = form.cleaned_data.get('phone1')
            user.employee.phone2 = form.cleaned_data.get('phone2')
            user.employee.email = form.cleaned_data.get('email')
            user.employee.address = form.cleaned_data.get('address')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            messages.success(
                request, f'สมัครสมาชิกสำเร็จ')
            return redirect('/employee')
    else:
        form = UserRegisterForm()
    return render(request, 'user/signup.html', {'form': form})


@login_required
def editProfile(request):
    myProfile = Employee.objects.get(id=request.user.id)
    if request.method == 'POST':
        myProfileform = UserRegisterForm(
            request.POST or None, instance=myProfile)
        if not myProfileform.is_valid():
            myProfileform.cleaned_data.get('fname')
            myProfile.fname = myProfileform.cleaned_data.get('fname')
            myProfile.lname = myProfileform.cleaned_data.get('lname')
            myProfile.id_card = myProfileform.cleaned_data.get('id_card')
            myProfile.phone1 = myProfileform.cleaned_data.get('phone1')
            myProfile.phone2 = myProfileform.cleaned_data.get('phone2')
            myProfile.email = myProfileform.cleaned_data.get('email')
            myProfile.address = myProfileform.cleaned_data.get('address')
            myProfile.save()
        messages.success(
                request, f'แก้ไขข้อมูลสำเร็จ')
        return redirect('/')
    else:
        form = UserRegisterForm(instance=myProfile)
    return render(request, 'user/editProfile.html', {'form': form})


@login_required
def profile(request):
    employee = Employee.objects.get(id=request.user.id)
    # messages.success(request, f'this is {employee.fname} profile!')
    return render(request, 'user/profile.html', {'employee': employee})
