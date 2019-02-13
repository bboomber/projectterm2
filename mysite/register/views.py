from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def register(request):
    return render(request, 'register/register.html')