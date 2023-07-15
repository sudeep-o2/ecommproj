from django.contrib import admin
from . models import Product
# Register your models here.
@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ['id','title','price','category','image']