from django.shortcuts import render
from . models import Product
# Create your views here.
def home(request):

    return render(request,'home.html')

def categories(request,pk):

    
    category_products = Product.objects.filter(category=pk)
    context={'category_products':category_products}
    return render(request,'ecommapp/categories.html',context)

def productDetail(request,pk):

    product_detail = Product.objects.get(id=pk)
    context={'product_detail':product_detail}
    return render(request,'ecommapp/detail.html',context)