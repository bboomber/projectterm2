from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import registerform, RegisterUserForm

# Create your views here.

def register(request):
    context = [
        RegisterUserForm("agent_code", "Agent Code"),
        RegisterUserForm("fname", "First Name"),
        RegisterUserForm("lname", "Last Name")
    ]
    return render(request, 'register/register.html', {'form': context})

def saveData(request):
    return HttpResponse("Completed")