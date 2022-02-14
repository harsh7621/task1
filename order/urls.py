from django.contrib import admin
from django.urls import path
from order import views

urlpatterns = [
	path('home',views.order,name="home"),
	path('delete/<int:id>',views.order_delete,name="delete"),
	path('add_data',views.order_add,name="add_data"),
	# path('add_data/<int:id>',views.add_data,name="add_data"),
	path('edit_data/<int:id>',views.order_add,name="edit_data"),
	path('price_data',views.price_data,name="price_data")

  
]