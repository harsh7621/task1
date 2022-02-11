from django.shortcuts import render,redirect
from order.models import Order
from customer.models import Customer
from product.models import Product
# Create your views here.

def list_order(request):
    data_fetch = Order.objects.all()
    return render(request,'list_order.html', {'data_fetch':data_fetch})

def delete_order(request, id):
    order_delete = Order.objects.filter(id=id)
    order_delete.delete()
    return redirect ('/home')

def add_data(request):
    customer_data = Customer.objects.all()
    product_data = Product.objects.all()
    return render(request,'add_data.html',{'customer_data':customer_data,'product_data':product_data})

def data_store(request):
    if request.method == 'POST':
        customer_name = request.POST['customer']
        product_name = request.POST['product']
        price = request.POST['price']
        qty = request.POST['qty']
        total_price = request.POST['total']
        order_store_data = Order(customer_id=Customer(customer_name),product_id=Product(product_name),Unit_price=price,qty=qty,total_price=total_price)
        order_store_data.save()
        return redirect('/home')

def edit_data(request,id):
    order_edit = Order.objects.filter(id=id)
    customer_edit = Customer.objects.filter(id=id)
    product_edit = Product.objects.filter(id=id)
    return render(request, 'edit.html', {'order_edit':order_edit,'customer_edit':customer_edit,'product_edit':product_edit})

def data_update(request,id):
    if request.method == 'POST':
        customer_name = request.POST['customer']
        product_name = request.POST['product']
        price = request.POST['price']
        qty = request.POST['qty']
        total_price = request.POST['total']
        order_store_dataa = Order(id=id,customer_id=Customer(customer_name),product_id=Product(product_name),Unit_price=price,qty=qty,total_price=total_price)
        order_store_dataa.save()
        return redirect('/home')
