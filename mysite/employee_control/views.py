from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Employee

# Create your views here.

def viewAllEmp(request):
    emp_list = Employee.objects.order_by('agent_code')
    return render(request, 'employee_control/viewAllEmp.html', {'emp_list': emp_list})

def viewEmpDetail(request, agent_code):
    employee = get_object_or_404(Employee, pk=agent_code)
    return render(request, 'employee_control/viewEmpDetail.html', {'employee': employee})