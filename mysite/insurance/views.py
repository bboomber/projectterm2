from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import InsureForm
from .models import Insure
from django.contrib.auth import login as auth_login, authenticate, login
from django.contrib.auth.models import User
from employee_control.models import Employee


@login_required
def sellInsure(request):
    if request.method == 'POST':
        form = InsureForm(request.POST)
        if form.is_valid():
            doc_nbr = form.cleaned_data.get('doc_nbr')
            package_id = form.cleaned_data.get('package_id')
            car_id = form.cleaned_data.get('car_id')
            car_number = form.cleaned_data.get('car_number')
            company_order = form.cleaned_data.get('company_order')
            price = form.cleaned_data.get('price')
            total_price = form.cleaned_data.get('total_price')
            post_date = form.cleaned_data.get('post_date')

            employee = Employee.objects.get(id=request.user.id)

            i = Insure(doc_nbr=doc_nbr, agent_code=employee,
                       car_number=car_number, company_order=company_order,
                       price=price, total_price=total_price,
                       post_date=post_date)
            i.save()
            return HttpResponseRedirect('/')
    else:
        form = InsureForm()
    return render(request, 'insurance/sellInsure.html', {'form': form})
