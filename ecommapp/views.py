from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Product,Customer
from . forms import CustomUserForm,CustomerForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):

    return render(request,'home.html')

def aboutus(request):
    return render(request,'ecommapp/about.html')


def loginView(request):
    stat='login'
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
        except:
            return HttpResponse('unable to login')
    context={'stat':stat}
    return render(request,'ecommapp/login_register.html',context)

def logoutView(request):

    logout(request)
    return redirect('home')

def register(request):

    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')

    context={'form':form}
    return render(request,'ecommapp/login_register.html',context)

def categories(request,pk):

    category_products = Product.objects.filter(category=pk)
    context={'category_products':category_products}
    return render(request,'ecommapp/categories.html',context)

def productDetail(request,pk):

    product_detail = Product.objects.get(id=pk)
    context={'product_detail':product_detail}
    return render(request,'ecommapp/detail.html',context)

def profile(request):

    form=CustomerForm()

    if request.method=='POST':
        customer=Customer.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            locality=request.POST.get('locality'),
            city=request.POST.get('city'),
            pincode=request.POST.get('pincode'),
            state=request.POST.get('state'),
            mobileno=request.POST.get('mobileno'),

        )
        return redirect('profile')

    context={'form':form}
    return render(request,'ecommapp/profile.html',context)

def adress(request):

    adresses=Customer.objects.filter(user=request.user)
    context={'adresses':adresses}
    return render(request,'ecommapp/adress.html',context)

def updateAdress(request,pk):

    up=Customer.objects.get(id=pk)
    form=CustomerForm(instance=up)

    if request.method=='POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            up=Customer.objects.get(id=pk)
            up.name=request.POST.get('name')
            up.locality=request.POST.get('locality')
            up.city=request.POST.get('city')
            up.pincode=request.POST.get('pincode')
            up.state=request.POST.get('state')
            up.mobileno=request.POST.get('mobileno')
            up.save()
            return redirect('adress')

    context={'form':form}
    return render(request,'ecommapp/updateadress.html',context)