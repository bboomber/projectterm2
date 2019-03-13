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
            # login(request, user)
            return redirect('/employee')
            # form.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}! You can login now')
            # return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/signup.html', {'form': form})

@login_required
def profile(request):
    employee = Employee.objects.get(id=request.user.id)
    return render(request, 'user/profile.html', {'employee': employee})

