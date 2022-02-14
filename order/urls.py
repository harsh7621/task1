from django.contrib import admin
from django.urls import path
from order import views

urlpatterns = [
	path('home',views.list_order,name="home"),
	path('delete/<int:id>',views.delete_order,name="delete"),
	path('add_data',views.add_data,name="add_data"),
	# path('add_data/<int:id>',views.add_data,name="add_data"),
	path('edit_data/<int:id>',views.edit_data,name="edit_data"),
	path('dataa',views.dataa,name="dataa")

  
]