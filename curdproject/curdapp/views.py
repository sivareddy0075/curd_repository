from django.shortcuts import render
from .models import ProductData
from .forms import InsertDataForm,UpdateDataForm,DeleteDataForm
from django.http.response import HttpResponse
def home_view(request):
    return render(request,'curd_home.html')


def insert_view(request):
    if request.method =="POST":
        iform = InsertDataForm(request.POST)
        if iform.is_valid():
            product_id = request.POST.get('product_id','')
            product_name = request.POST.get('product_name','')
            product_cost = request.POST.get('product_cost','')
            product_color = request.POST.get('product_color','')
            product_class = request.POST.get('product_class','')
            customer_name = request.POST.get('customer_name','')
            customer_mobile = request.POST.get('customer_mobile','')
            customer_email = request.POST.get('customer_email','')

            data = ProductData(product_id=product_id,
                        product_name=product_name,
                        product_class=product_class,
                        product_cost=product_cost,
                        product_color=product_color,
                        customer_name=customer_name,
                        customer_mobile=customer_mobile,
                        customer_email=customer_email)
            data.save()
            iform = InsertDataForm()
            return render(request,'curd_insert.html',{'iform':iform})

        else:
            return HttpResponse("Invalid Form")
    else:
        iform = InsertDataForm()
        return render(request,'curd_insert.html',{'iform':iform})


def fetch_view(request):
    pdata = ProductData.objects.all()
    return render(request,'curd_fetch.html',{'pdata':pdata})


def update_view(request):
    if request.method =="POST":
        uform = UpdateDataForm(request.POST)
        if uform.is_valid():
            product_id = request.POST.get('product_id','')
            product_cost = request.POST.get('product_cost','')

            pid = ProductData.objects.filter(product_id=product_id)

            if not pid:
                return HttpResponse("Product Id is not available")
            else:
                pid.update(product_cost=product_cost)
                uform = UpdateDataForm()
                return render(request,'curd_update.html',{'uform':uform})

    else:
        uform = UpdateDataForm()
        return render(request,'curd_update.html',{'uform':uform})


def delete_view(request):
    if request.method =="POST":
        dform = DeleteDataForm(request.POST)
        if dform.is_valid():
            product_id = request.POST.get('product_id','')

            pid = ProductData.objects.filter(product_id=product_id)

            if not pid:
                return HttpResponse("Product Id Is Not Available")
            else:
                pid.delete()
                dform = DeleteDataForm()
                return render(request, 'curd_delete.html', {'dform': dform})
    else:
        dform = DeleteDataForm()
        return render(request,'curd_delete.html',{'dform':dform})


