from django.contrib import admin
from . models import Product,Customer,Cart,Payment,OrderPlaced
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

@admin.register(Payment)
class PaymentAdminModel(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

@admin.register(OrderPlaced)
class OrderPlacedAdminModel(admin.ModelAdmin):  
    list_display = ['id','user','customer','product','quantity','order_date','status','payment']