from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Employee
from insurance.models import Insure
from django.contrib.auth.models import User, Permission
from operator import itemgetter
from .forms import Roleform
from user.forms import UserRegisterForm

# Create your views here.


@login_required
def viewAllEmp(request):
    emp_list = Employee.objects.order_by('id')
    return render(request, 'employee_control/viewAllEmp.html', {'emp_list': emp_list})


@login_required
def viewEmpDetail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employee_control/viewEmpDetail.html', {'employee': employee})



# def remind(request):
#     all_month = []
#     month_list = ['มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม',
#                   'มิถุนายน', 'กรกฎาคม', 'สิงหาคม', 'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม']
    
#     for i in range(len(month_list)):
#         month = MyMonth()
#         this_num = i + 1
#         month.month_num = this_num
#         month.month_name = month_list[i]
#         all_month.append(month)
#         month.ins_list = Insure.objects.filter(post_date__month=this_num, agent_code=request.user.id)
#     return render(request, 'employee_control/remind.html', {'all_month': all_month})

def remind(request):
    # all_list = Insure.objects.filter(post_date__month=1, agent_code=request.user.id).order_by('-id')
    emp_id = Employee.objects.get(user = request.user.id)
    month_list = list(Insure.objects.filter(post_date__month=1, agent_code=emp_id))
    month_list = sorted(month_list, key=lambda i: i.post_date.day)

    return render(request, 'employee_control/notice/notice1.html', {'month_list': month_list})

def remind2(request):
    emp_id = Employee.objects.get(user = request.user.id)
    month_list = Insure.objects.filter(post_date__month=2, agent_code=emp_id)
    month_list = sorted(month_list, key=lambda i: i.post_date.day)
    return render(request, 'employee_control/notice/notice2.html', {'month_list': month_list})

def remind3(request):
    emp_id = Employee.objects.get(user = request.user.id)
    month_list = Insure.objects.filter(post_date__month=3, agent_code=emp_id)
    month_list = sorted(month_list, key=lambda i: i.post_date.day)
    return render(request, 'employee_control/notice/notice3.html', {'month_list': month_list})

def remind4(request):
    emp_id = Employee.objects.get(user = request.user.id)
    month_list = Insure.objects.filter(post_date__month=4, agent_code=emp_id)
    month_list = sorted(month_list, key=lambda i: i.post_date.day)
    return render(request, 'employee_control/notice/notice4.html', {'month_list': month_list})

def remind5(request):
    emp_id = Employee.objects.get(user = request.user.id)
    month_list = Insure.objects.filter(post_date__month=5, agent_code=emp_id)
    month_list = sorted(month_list, key=lambda i: i.post_date.day)
    return render(request, 'employee_control/notice/notice5.html', {'month_list': month_list})

def remind6(request):
    emp_id = Employee.objects.get(user = request.user.id)
    month_list = Insure.objects.filter(post_date__month=6, agent_code=emp_id)
    month_list = sorted(month_list, key=lambda i: i.post_date.day)
    return render(request, 'employee_control/notice/notice6.html', {'month_list': month_list})

def remind7(request):
    emp_id = Employee.objects.get(user = request.user.id)
    month_list = Insure.objects.filter(post_date__month=7, agent_code=emp_id)
    month_list = sorted(month_list, key=lambda i: i.post_date.day)
    return render(request, 'employee_control/notice/notice7.html', {'month_list': month_list})

def remind8(request):
    emp_id = Employee.objects.get(user = request.user.id)
    month_list = Insure.objects.filter(post_date__month=8, agent_code=emp_id)
    month_list = sorted(month_list, key=lambda i: i.post_date.day)
    return render(request, 'employee_control/notice/notice8.html', {'month_list': month_list})

def remind9(request):
    emp_id = Employee.objects.get(user = request.user.id)
    month_list = Insure.objects.filter(post_date__month=9, agent_code=emp_id)
    month_list = sorted(month_list, key=lambda i: i.post_date.day)
    return render(request, 'employee_control/notice/notice9.html', {'month_list': month_list})

def remind10(request):
    emp_id = Employee.objects.get(user = request.user.id)
    month_list = Insure.objects.filter(post_date__month=10, agent_code=emp_id)
    month_list = sorted(month_list, key=lambda i: i.post_date.day)
    return render(request, 'employee_control/notice/notice10.html', {'month_list': month_list})

def remind11(request):
    emp_id = Employee.objects.get(user = request.user.id)
    month_list = Insure.objects.filter(post_date__month=11, agent_code=emp_id)
    month_list = sorted(month_list, key=lambda i: i.post_date.day)
    return render(request, 'employee_control/notice/notice11.html', {'month_list': month_list})

def remind12(request):
    emp_id = Employee.objects.get(user = request.user.id)
    month_list = Insure.objects.filter(post_date__month=12, agent_code=emp_id)
    month_list = sorted(month_list, key=lambda i: i.post_date.day)
    return render(request, 'employee_control/notice/notice12.html', {'month_list': month_list})


class MyMonth(object):
    month_num = 1
    month_name = ""
    ins_list = []



def editRole(request, id):
    this_profile = Employee.objects.get(user=id)
    this_user = User.objects.get(id=id)
    print(this_user, this_profile.role)
    role = Roleform()
    if request.method == 'POST':
        role = Roleform(request.POST or None)
        if role.is_valid():
            emp_role = role.cleaned_data.get('role')
            this_user.user_permissions.clear()
            if emp_role == 'admin':
                this_user.user_permissions.add(Permission.objects.get(name='Role is admin'))
                this_profile.role = 'admin'
                this_profile.save()
                print(this_user.has_perm('employee_control.is_admin'), this_profile.role)
            elif emp_role == 'manager':
                this_user.user_permissions.add(Permission.objects.get(name='Role is manager'))
                this_profile.role = 'manager'
                this_profile.save()
                print(this_user.has_perm('employee_control.is_manager'), this_profile.role)
            elif emp_role == 'broker':
                this_profile.role = 'broker'
            this_profile.save()
    return render(request, 'employee_control/editRole.html', { 'role':role})
