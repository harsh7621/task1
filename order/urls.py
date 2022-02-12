from django.contrib import admin
from django.urls import path
from order import views

urlpatterns = [
	path('home',views.list_order,name="home"),
	path('delete/<int:id>',views.delete_order,name="delete"),
	path('add_data',views.add_data,name="add_data"),
	path('data_store',views.data_store,name="data_store"),
	path('edit/<int:id>',views.edit_data,name="edit"),
	path('data_update/<int:id>',views.data_update,name="data_update"),
	path('dataa',views.dataa,name="dataa")

  
]