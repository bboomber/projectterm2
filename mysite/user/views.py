from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages

from .forms import UserRegisterForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/employee')
    else:
        form = UserRegisterForm()
    return render(request, 'user/signup.html', {'form': form})
