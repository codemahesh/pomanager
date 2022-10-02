from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import CustomerForm, CustomerPoForm,  CustomerRegistration, UomForm
from .models import Customer, CustomerPo, Uom
from django.contrib.admin.widgets import AdminDateWidget
from django.http import JsonResponse
import json

def customer(request):
    return 

def customer_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = CustomerForm()
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(instance=customer)
        return render(request,'customer_register/customer_form.html',{'form':form})
    else:
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/customer/list')
    
def customer_list(request):
    context = {'customer_list':Customer.objects.all()}
    return render(request,'customer_register/customer_list.html', context)


# new video

#Create your views here.

def add_show(request):
    if request.method == 'POST':
        form = CustomerRegistration(request.POST)
        if form.is_valid():
            name_var = form.cleaned_data['customer_name']
            code_var = form.cleaned_data['customer_code']
            category_var = form.cleaned_data['category']
            address_var = form.cleaned_data['address']
            place_var = form.cleaned_data['place']
            reg = Customer(customer_name = name_var, customer_code = code_var, category = category_var, address = address_var, place = place_var )
            reg.save()
            form = CustomerRegistration()
    else:
        form = CustomerRegistration()
    cust = Customer.objects.all()

    return render (request,'customer/addandshow.html',{'form':form,'cust':cust})

# Delete customer name

def delete_data(request,id):
    if request.method == 'POST':
        pi = Customer.objects.get(pk=id)
        pi.delete()
        return redirect('addandshow')

# Edit or update customer name

def update_data(request, id):
    customer_id = Customer.objects.get(pk=id)
    form = CustomerRegistration(request.POST or None, instance = customer_id)
    if form.is_valid():
        form.save()
        return redirect('addandshow')   
    return render(request, 'customer/update.html', {'form': form})


def unit_add(request):
    if request.method == 'POST':
        form = UomForm(request.POST)
        if form.is_valid():
            form.save()
        form = UomForm()
    else:
        form = UomForm()
    all_unit=Uom.objects.all() 
    return render(request,'unit/addunit.html',{'form':form,'all_unit':all_unit})

def unit_update(request, id):
    unit_id = Uom.objects.get(pk=id)
    form = UomForm(request.POST or None, instance = unit_id)
    if form.is_valid():
        form.save()
        return redirect('addunit')   
    return render(request, 'unit/updateunit.html', {'form': form })

def unit_delete(request, id):
    if request.method == 'POST':
        unit= Uom.objects.get(pk=id)
        unit.delete()
        return redirect('addunit')

def customer_po_add(request):
    if request.method == 'POST':
        form = CustomerPoForm(request.POST)
        if form.is_valid():
            form.save()
            
        form = CustomerPoForm()
        # cutomer_po_number = request.POST.get('customer_po_number')
        # date = request.POST.get('date')
        # code = request.POST.get('code')
        # customer_name = request.POST.get('customer_name')
        # form = CustomerPo(cutomer_po_number=cutomer_po_number, date = date, code=code, customer_name=customer_name)
        # form.save()
        
    else:
        form = CustomerPoForm()

    customer_code = Customer.objects.all()


    return render(request,'customerpo/addcustomerpoform.html',{'form':form, 'customer_code':customer_code})


def getCustomerCode(request):
    data = json.loads(request.body)
    customer_code = data["id"]
    customer = Customer.objects.filter(customer_code=customer_code)
    print(customer_code)
    return JsonResponse(list(customer.values("customer_name")), safe=False)


def fillcustomercode(request):
    data= json.loads(request.body)
    customer_name = data["id"]
    customer =  Customer.objects.filter(customer_name=customer_name)
    return JsonResponse("It is also working", safe=False)
    # data = json.loads(request.body)
    # customer_name = data['id']