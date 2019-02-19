from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Employee
from .forms import Nameform

# Create your views here.

def viewAllEmp(request):
    emp_list = Employee.objects.order_by('agent_code')
    return render(request, 'employee_control/viewAllEmp.html', {'emp_list': emp_list})

def viewEmpDetail(request, agent_code):
    employee = get_object_or_404(Employee, pk=agent_code)
    return render(request, 'employee_control/viewEmpDetail.html', {'employee': employee})

def get_name(request):
    if request.method =='POST':
        form = Nameform(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thank/')
    else:
        form = Nameform()
    return render(request, 'employee_control/name.html', {'form': form})