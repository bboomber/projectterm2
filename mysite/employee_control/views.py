from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import Nameform

# Create your views here.

@login_required
def viewAllEmp(request):
    emp_list = Employee.objects.order_by('id')
    return render(request, 'employee_control/viewAllEmp.html', {'emp_list': emp_list})

@login_required
def viewEmpDetail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employee_control/viewEmpDetail.html', {'employee': employee})

def get_name(request):
    if request.method =='POST':
        form = Nameform(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/employee/')
    else:
        form = Nameform()
    return render(request, 'employee_control/name.html', {'form': form})