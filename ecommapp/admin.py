from django.contrib import admin
from . models import Product,Customer,Cart
# Register your models here.
@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ['id','title','price','category','image']

@admin.register(Customer)
class CustomerAdminModel(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','pincode','state','mobileno']

@admin.register(Cart)
class CartAdminModel(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']