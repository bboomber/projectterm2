from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.
def showhome(request):
    return render(request, 'mysite/home.html')

def showQandA(request):
    return render(request, 'mysite/QandA.html')

def showContact(request):
    return render(request, 'mysite/contact.html')
