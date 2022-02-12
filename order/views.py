from django.shortcuts import render,redirect
from order.models import Order
from customer.models import Customer
from product.models import Product
from django.http import JsonResponse
# Create your views here.

def list_order(request):
    data_fetch = Order.objects.values("id","customer__first_name","product__product_name","Unit_price","qty","total_price")
    return render(request,'list_order.html', {'data_fetch':data_fetch})

def delete_order(request, id):
    order_delete = Order.objects.filter(id=id)
    order_delete.delete()
    return redirect ('/home')

def add_data(request):
    if request.method == 'POST':
        customer_name = request.POST['customer']
        product_name = request.POST['product']
        price = request.POST['price']
        qty = request.POST['qty']
        total_price = request.POST['total']
        order_store_data = Order(customer=Customer(customer_name),product=Product(product_name),Unit_price=price,qty=qty,total_price=total_price)
        order_store_data.save()
        return redirect('/home')
    else:
        customer_data = Customer.objects.values("id","first_name")
        product_data = Product.objects.values("id","product_name")
        return render(request,'order.html',{'customer_data':customer_data,'product_data':product_data})

def edit_data(request,id):
    if request.method == 'POST':
        customer_name = request.POST['customer']
        product_name = request.POST['product']
        price = request.POST['price']
        qty = request.POST['qty']
        total_price = request.POST['total']
        order_store_dataa = Order(id=id,customer=Customer(customer_name),product=Product(product_name),Unit_price=price,qty=qty,total_price=total_price)
        order_store_dataa.save()
        return redirect('/home')
    else:
        order_edit = Order.objects.filter(id=id)
        
        return render(request, 'order.html', {'order_edit':order_edit})

def dataa(request):
    if request.method == "POST":
        id=request.POST.get('product')
        print(id)
        pi=Product.objects.get(id=id)
        product_price=(pi.unit_price)
        return JsonResponse({'product_price':product_price})
    