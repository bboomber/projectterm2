from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Customer, Car
from .forms import CustomerForm, CarForm

# Create your views here.


def viewCusDetail(request, id):
    cus = get_object_or_404(Customer, id=id)
    return render(request,'customer/viewCusDetail.html', {'cus': cus})


def viewCarDetail(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, 'customer/viewCarDetail.html', {'car':car})

def showAllCar(request):
    car_list = Car.objects.order_by('id')
    return render(request, 'customer/showAllCar.html', {'car_list': car_list})


def showAllCus(request):
    cus_list = Customer.objects.order_by('id')
    return render(request, 'customer/showAllCus.html', {'cus_list': cus_list})


def newCar(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car_id = form.cleaned_data.get('car_id')
            car_number = form.cleaned_data.get('car_number')
            province = form.cleaned_data.get('province')
            chassis_number = form.cleaned_data.get('chassis_number')
            model = form.cleaned_data.get('model')
            brand = form.cleaned_data.get('brand')
            car_cc = form.cleaned_data.get('car_cc')
            car_type = form.cleaned_data.get('car_type')
            sit = form.cleaned_data.get('sit')

            car = Car(car_id=car_id, car_number=car_number,
                      province=province, chassis_number=chassis_number,
                      model=model, car_cc=car_cc,
                      car_type=car_type, sit=sit,
                      brand=brand)
            car.save()
            return HttpResponseRedirect('/')
    else:
        form = CarForm()
    return render(request, 'customer/newCar.html', {'form': form})


def newCus(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            cus_id = form.cleaned_data.get('cus_id')
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            address = form.cleaned_data.get('address')
            province = form.cleaned_data.get('province')
            zipcode = form.cleaned_data.get('zipcode')
            id_card = form.cleaned_data.get('id_card')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')

            cus = Customer(cus_id=cus_id, fname=fname,
                           lname=lname, address=address,
                           province=province, zipcode=zipcode,
                           id_card=id_card, phone=phone,
                           email=email)
            cus.save()
            return HttpResponseRedirect('/')
    else:
        form = CustomerForm()
    return render(request, 'customer/newCus.html', {'form': form})
