from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from order.models import Order
from customer.models import Customer
from product.models import Product
from django.http import JsonResponse
# Create your views here.

def order(request):
    data_fetch = Order.objects.values("id","customer__first_name","product__product_name","Unit_price","qty","total_price")
    paginator = Paginator(data_fetch, 5)
    page_number = request.GET.get('page')
    data_fetch = paginator.get_page(page_number)   
    return render(request,'list_order.html', {'data_fetch':data_fetch})

def order_delete(request,id):
    order_delete = Order.objects.filter(id=id)
    order_delete.delete()
    return redirect ('/')

def order_add(request,id=None):
    if request.method == 'POST':
        # form_id = request.POST['formid']
        customer_id = request.POST['customer']
        product_id = request.POST['product']
        price = request.POST['price']
        qty = request.POST['qty']
        total_price = request.POST['total']
        if(id==None):
            order_store_data = Order(customer_id=customer_id,product_id=product_id,Unit_price=price,qty=qty,total_price=total_price)
        else:
            order_store_data = Order(id=id,customer_id=customer_id,product_id=product_id,Unit_price=price,qty=qty,total_price=total_price)
        order_store_data.save()
        return redirect('/')
    else:
        if(id==None):
            customer_data = Customer.objects.values("id","first_name")
            product_data = Product.objects.values("id","product_name")
            return render(request,'order.html',{'customer_data':customer_data,'product_data':product_data})
        else:
            order_edit = Order.objects.filter(id=id)
            order_editt=order_edit.values("id","customer__id","customer__first_name","product__id","product__product_name","Unit_price","qty","total_price")
            return render(request,'order.html',{'order_edit':order_editt})

def price_data(request):
    if request.method == "POST":
        id=request.POST.get('product')
        # print(id)
        pi=Product.objects.get(id=id)
        product_price=(pi.unit_price)
        return JsonResponse({'product_price':product_price})
    