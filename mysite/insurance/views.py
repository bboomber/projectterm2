# !usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import InsureForm, TranferForm, InsureEditForm, SellingForm, EdittingForm
from employee_control.forms import Empform
from package_control.forms import PackageForm
from customer.forms import CarForm, CustomerForm
from .models import Insure, Tranfer
from django.contrib.auth import login as auth_login, authenticate, login
from django.contrib.auth.models import User
from employee_control.models import Employee
from customer.models import Car, Customer
from package_control.models import Package
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
import uuid
from datetime import date

from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf, link_callback

from io import BytesIO
from xhtml2pdf import pisa
from django.template import Context

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        # response = render(request, 'insurance/invoice.html')
        template_path = 'insurance/invoice.html'
        context = {'hi': 'hello, world'}
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)
        # create a pdf
        pisaStatus = pisa.CreatePDF(html, dest=response, encoding='utf-8', link_callback=link_callback)
        # if error then show some funy view
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
        
def turnToPDF(request, id):
    insure = Insure.objects.get(id=id)

    template_path = 'insurance/invoice.html'
    response = HttpResponse(content_type='application/pdf')
    template = get_template(template_path)
    html = template.render({'insure': insure,
        'car': insure.car_id,
        'cus': insure.cus_id,
        'pack': insure.package_id,
        'enddate': (insure.post_date.year)+1
        })
    pisaStatus = pisa.CreatePDF(html, dest=response, encoding='utf-8', link_callback=link_callback)
    return response

def delInsure(request, id):
    insure = Insure.objects.get(id=id)
    if request.method=='POST':
        confirm = request.POST['subject']
        if confirm =='yes':
            Insure.objects.get(id=id).delete()
            messages.success(request, f'ลบกรมธรรม์แล้ว')
        else:
            messages.warning(request, f'ยังไม่ได้ลบกรมธรรม์')
        insure.save()
        return redirect('/')
    return render(request, 'insurance/delInsure.html', {'insure': insure})

@login_required
def viewInsureDetail(request, id):
    insure = get_object_or_404(Insure, id=id)
    return render(request, 'insurance/viewInsureDetail.html', {'insure': insure})

@login_required
def editInsure(request, id):
    myInsure = Insure.objects.get(id=id)
    editForm = EdittingForm()
    cus = myInsure.cus_id
    package = myInsure.package_id
    car = myInsure.car_id
    emp = myInsure.agent_code
    context_edit = {
        'cus_fname': cus.fname,'cus_lname': cus.lname,'cus_address': cus.address,'cus_province': cus.province,
        'cus_zipcode': cus.zipcode,'cus_id_card': cus.id_card, 'cus_phone': cus.phone,'cus_email': cus.email,

        'car_number': car.car_number,'car_province': car.province,'car_brand': car.brand,'car_chassis_number': car.chassis_number,
        'car_model': car.model,'car_cc': car.car_cc,'car_type': car.car_type,'car_sit': car.sit,

        'package_name': package.package_name
    }
    if request.method =="POST":
        # form = InsureForm(request.POST or None)
        editForm = EdittingForm(request.POST or None)
        if not editForm.is_valid():
            cus.fname=editForm.cleaned_data.get('cus_fname')
            cus.lname=editForm.cleaned_data.get('cus_lname')
            cus.address=editForm.cleaned_data.get('cus_address')
            cus.province=editForm.cleaned_data.get('cus_province')
            cus.zipcode=editForm.cleaned_data.get('cus_zipcode')
            cus.id_card=editForm.cleaned_data.get('cus_id_card')
            cus.phone=editForm.cleaned_data.get('cus_phone')
            cus.email=editForm.cleaned_data.get('cus_email')
            cus.save()
            car.car_number=editForm.cleaned_data.get('car_number')
            car.province=editForm.cleaned_data.get('car_province')
            car.brand=editForm.cleaned_data.get('car_brand')
            car.chassis_number=editForm.cleaned_data.get('car_chassis_number')
            car.model=editForm.cleaned_data.get('car_model')
            car.car_cc=editForm.cleaned_data.get('car_cc')
            car.car_type=editForm.cleaned_data.get('car_type')
            car.sit=editForm.cleaned_data.get('car_sit')
            car.save()
            messages.success(request, f'แก้ไขกรมธรรม์สำเร็จ')
        return redirect('/')
    else:
        # form = InsureForm(initial=context)
        editForm = EdittingForm(initial=context_edit)
    return render(request, 'insurance/editInsure.html', {
        'myInsure': myInsure,
        'editform': editForm
        })

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
            employee = Employee.objects.get(user=request.user.id)
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

@permission_required('employee_control.is_manager', raise_exception=True)
def setConfirm(request, id):
    insure = Insure.objects.get(id=id)
    emp = Employee.objects.get(id=insure.agent_code_id)
    car = Car.objects.get(id=insure.car_id_id)
    cus = Customer.objects.get(id=insure.cus_id_id)
    pack = Package.objects.get(id= insure.package_id_id)
    pic = Tranfer.objects.filter(emp_id = emp).last()
    print(pic.pic_balance)
    if request.method=='POST':
        confirm = request.POST['subject']
        if confirm =='yes':
            insure.confirm = 1
            messages.success(request, f'อนุมัติกรมธรรมเรียบร้อยแล้ว')
        else:
            insure.delete()
            messages.warning(request, f'คุณไม่อนุมัติกรมธรรม์')
        insure.save()
        return redirect('/')
    return render(request, 'insurance/setConfirm.html', {'insure': insure, 'car': car, 'cus': cus, 'pack': pack, 'emp': emp, 'pic':pic})

@permission_required('employee_control.is_manager', raise_exception=True)
def showConfirmInsure(request):
    ins_list = Insure.objects.filter(confirm=2)
    return render(request, 'insurance/showConfirmInsure.html', {'ins_list': ins_list})

@permission_required('employee_control.is_manager', raise_exception=True)
def showAllInsure(request):
    ins_list = Insure.objects.filter(confirm=1).order_by('id')[:1000]
    return render(request, 'insurance/showAllInsure.html', {'ins_list': ins_list})

@permission_required('employee_control.is_manager', raise_exception=True)
def showReport(request):
    return render(request, 'insurance/showReport.html')

@permission_required('employee_control.is_manager', raise_exception=True)
def showPredict(request):
    months = ['January', 'February', 'March', 'April', 'May', \
        'June', 'July', 'August', 'September', 'October', 'November', 'December']
    insure_list = {}
    insure_count = []

    for year in range(2015, 2017):
        for month in range(1, 13):
            ins_monthly_count = Insure.objects.filter(post_date__year=year, post_date__month=month).count()
            insure_count.append(ins_monthly_count)
    
    insure_list[str(2017)] = predictSale(insure_count)

    return render(request, 'insurance/showPredict.html', {'months': months, 'insure_list': insure_list})

@login_required
def showEmpInsure(request):
    emp_id = Employee.objects.get(user = request.user.id)
    ins_list = Insure.objects.filter(agent_code = emp_id, confirm=1)[:800]
    return render(request, 'insurance/showEmpInsure.html', {'ins_list': ins_list})

@login_required
def newCusSell(request):
    pic = []
    if request.method=='POST':
        pic = Tranfer.objects.get(id=1).pic_balance
        tranForm = TranferForm(request.POST, request.FILES)
        if tranForm.is_valid():
            t = Tranfer.objects.get(id=1)
            t.pic_balance = tranForm.cleaned_data['pic_balance']
            t.save()
            print('save jaa')
        else:
            print('hi')
        #Tranfer.objects.get(id=1).pic_balance.delete(save=True)
    else:
        tranForm = TranferForm()
        
    return render(request, "insurance/newCusSell.html", {'pic': pic, 'tranForm': tranForm})

def newSelling(request):
    if request.method == 'POST':
        form = SellingForm(request.POST, request.FILES)
        if form.is_valid():
            package = Package.objects.get(package_id=form.cleaned_data.get('package_id'))
            total_price= package.price + (package.price*7/100)
            # -----------------cusForm-------------------
            cus = Customer(
                cus_id="",
                fname=form.cleaned_data.get('cus_fname'),
                lname=form.cleaned_data.get('cus_lname'),
                address=form.cleaned_data.get('cus_address'),
                province=form.cleaned_data.get('cus_province'),
                zipcode=form.cleaned_data.get('cus_zipcode'),
                id_card=form.cleaned_data.get('cus_id_card'),
                phone=form.cleaned_data.get('cus_phone'),
                email=form.cleaned_data.get('cus_email')
            )
            cus.save()
            this_cus = Customer.objects.latest('id')
            print(this_cus)
            # -------emp---------------
            employee = Employee.objects.get(user=request.user.id)
            # ------------car-----------------
            car = Car(
                car_id="",
                car_number=form.cleaned_data.get('car_number'),
                province=form.cleaned_data.get('car_province'),
                brand=form.cleaned_data.get('car_brand'),
                chassis_number=form.cleaned_data.get('car_chassis_number'),
                model=form.cleaned_data.get('car_model'),
                car_cc=form.cleaned_data.get('car_cc'),
                car_type=form.cleaned_data.get('car_type'),
                sit=form.cleaned_data.get('car_sit'))
            car.save()
            this_car = Car.objects.latest('id')
            print(this_car)
            # ---------------Tranfer-----------------------
            tran = Tranfer(
                emp_id=employee,
                Package_id=package,
                balance=total_price,
                pic_balance=form.cleaned_data['pic_balance'])
            tran.save()
            doc_nbr = uuid.uuid4().hex[:12].upper()
            ins = Insure(doc_nbr=doc_nbr, agent_code=employee,
                         package_id=package,
                         car_id=this_car, car_number=this_car.car_number,
                         cus_id=this_cus,
                         company_order=package.company_name,
                         price=package.price, total_price=total_price,
                         post_date=date.today())
            ins.save()
            your_ins = Insure.objectslatest('id')
            # messages.success(request, f'ได้รับข้อมูลกรมธรรม์แล้ว อยู่ระหว่างการรออนุมัติกรมธรรม์')
            messages.success(request, f'ออกกรมธรรม์สำเร็จแล้ว <a href="/"></a>')
            return HttpResponseRedirect('/')
    else:
        form = SellingForm()
    return render(request, 'insurance/newSelling.html', {'form': form})




# Predict Sale by year
def predictSale(insure_list):
    alpha = 0.1341
    beta = 0.8575
    gamma = 0.8082
    value = insure_list

    ls = int(0)
    yl = int(0)

    mad_avg  = int(0)
    mape_avg = int(0)

    sl = []
    at = []
    bt = []
    st = []
    ft = []

    mad  = []
    mape = []

    count_at = int(1)
    count_bt = int(0)
    count_st = int(13)
    count_stl = int(0)

    #LS At
    for l in range(12):
        ls += value[l]
    ls = ls/12
    # print("Ls: ", ls)

    #Yl+t-Yt
    for y in range(0, 12, 1):
        yl += value[12+y]-value[0+y]
    # print(yl)

    #Bs Tt
    yl = yl/12**2
    # print("Bs: ", yl)

    #Sl St
    for s in range(0, 12, 1):
        sl.insert(s, value[s]-ls)
    # print("St-L+m: ", sl)

    #At
    at.insert(0, alpha*(value[12]-sl[0])+(1-alpha)*(ls+yl))

    #bt
    bt.insert(0, beta*(at[0]-ls)+(1-beta)*yl)

    #st
    st.insert(0, gamma*(value[12]-at[0])+(1-gamma)*(sl[0]))

    #At
    for atl in range(13, 24, 1):
        at.insert(count_at, alpha*(value[atl]-sl[count_at])+(1-alpha)*(at[count_at-1]+bt[count_at-1]))
        

        #bt
        bt.insert(count_bt+1, beta*(at[count_bt+1]-at[count_bt])+(1-beta)*bt[count_bt])
        count_bt += 1

        #st
        st.insert(count_at, gamma*(value[count_st]-at[count_at])+(1-gamma)*(sl[count_at]))
        count_st += 1
        count_at += 1


    #At2
    for atl in range(24, len(value), 1):
        at.insert(count_at, alpha*(value[atl]-st[count_stl])+(1-alpha)*(at[count_at-1]+bt[count_at-1])) 

        #bt2
        bt.insert(count_bt+1, beta*(at[count_bt+1]-at[count_bt])+(1-beta)*bt[count_bt])
        count_bt += 1

        #st2
        st.insert(count_at, gamma*(value[count_st]-at[count_at])+(1-gamma)*(st[count_stl]))
        count_st += 1
        count_at += 1
        count_stl += 1

    ft.insert(0, (ls+yl)+st[0])
    for j in range(0, len(value)-13, 1):
        ft.insert(j+1, (at[j]+bt[j])+st[j+1])

    #print
    for i in range(0, len(value)-12, 1):   
        # print("Period:", 13+i, "| Y: ", value[i+12], "| At:", at[i], "| bt:", bt[i], "| St:", st[i], "| ft:", ft[i], "| mad:", abs(value[i+12]-ft[i]), "| mape:",(abs(value[i+12]-ft[i])*100)/value[i+12] )
        mad.insert(i, abs(value[i+12]-ft[i]))
        mape.insert(i, (mad[i]*100)/value[i+12])

    #mad average
    for m in mad:
        mad_avg += m
    print("mad avg: ", (mad_avg/len(mad)))

    #mape average
    for ma in mape:
        mape_avg += ma

    mape_avg = mape_avg/len(mape)
    st_pd = []
    pd = []
   
    #Predict
    for m in range(len(st)-1, len(st)-13, -1):
        st_pd.insert(0, (st[m]))
        pd.insert(0, (at[len(at)-1]+bt[len(bt)-1])+st[m]+(m+1))

    predict_sale = []
    for j in range(0, 12, 1):
        predict_sale.append(pd[j])
        # print("month : ", j+1 , "| St: ", st_pd[j], "| Predict: ", pd[j])
    
    return predict_sale