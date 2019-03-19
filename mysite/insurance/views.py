from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import InsureForm
from .models import Insure
from django.contrib.auth import login as auth_login, authenticate, login
from django.contrib.auth.models import User
from employee_control.models import Employee
from customer.models import Car, Customer
from package_control.models import Package


def viewInsureDetail(request, id):
    insure = get_object_or_404(Insure, id=id)
    return render(request, 'insurance/viewInsureDetail.html', {'insure': insure})


@login_required
def sellInsure(request):
    if request.method == 'POST':
        form = InsureForm(request.POST)
        if form.is_valid():
            doc_nbr = form.cleaned_data.get('doc_nbr')
            # ------------------------------------------
            pack_id = form.cleaned_data.get('package_id')
            package = Package.objects.get(package_id=pack_id)
            # ------------------------------------------
            car_id = form.cleaned_data.get('car_id')
            car = Car.objects.get(car_id=car_id)
            # ------------------------------------------
            cus_id = form.cleaned_data.get('cus_id')
            cus = Customer.objects.get(cus_id=cus_id)
            # ------------------------------------------
            company_order = form.cleaned_data.get('company_order')
            price = form.cleaned_data.get('price')
            total_price = form.cleaned_data.get('total_price')
            post_date = form.cleaned_data.get('post_date')
            # ------------------------------------------
            employee = Employee.objects.get(id=request.user.id)
            # ------------------------------------------
            ins = Insure(doc_nbr=doc_nbr, agent_code=employee,
                         package_id=package,
                         car_id=car, car_number=car.car_number,
                         cus_id=cus,
                         company_order=company_order,
                         price=price, total_price=total_price,
                         post_date=post_date)
            ins.save()
            return HttpResponseRedirect('/')
    else:
        form = InsureForm()
    return render(request, 'insurance/sellInsure.html', {'form': form})


@login_required
def showAllInsure(request):
    ins_list = Insure.objects.order_by('id')
    return render(request, 'insurance/showAllInsure.html', {'ins_list': ins_list})


def showReport(request):
    return render(request, 'insurance/showReport.html')


def showPredict(request):
    return render(request, 'insurance/showPredict.html')
