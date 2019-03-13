from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import PackageForm
from .models import Package

# Create your views here.


@login_required
def newPackage(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            package_id = form.cleaned_data.get('package_id')
            package_name = form.cleaned_data.get('package_name')
            company_name = form.cleaned_data.get('company_name')
            package_cc = form.cleaned_data.get('package_cc')
            package_type = form.cleaned_data.get('package_type')
            price = form.cleaned_data.get('price')
            detail = form.cleaned_data.get('detail')

            pack = Package(package_id=package_id, package_name=package_name,
                           company_name=company_name, package_cc=package_cc,
                           package_type=package_type, price=price,
                           detail=detail)
            pack.save()
            return HttpResponseRedirect('/')
    else:
        form = PackageForm()
    return render(request, 'package_control/newPackage.html', {'form': form})


@login_required
def showPackage(request):
    pack_list = Package.objects.order_by('id')
    return render(request, 'package_control/showPackage.html', {'pack_list': pack_list})


def showPromotion(request):
    return render(request, 'package_control/showPromotion.html')
