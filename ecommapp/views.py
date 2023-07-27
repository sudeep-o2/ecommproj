from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render,redirect
from . models import Product,Customer,Cart,Payment,OrderPlaced
from . forms import CustomUserForm,CustomerForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import razorpay
from django.conf import settings

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

def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart.objects.create(
        user=user,
        product=product,
    )
   
    return redirect('cart')


def show_cart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount=0
    for pr in cart:
        val=pr.quantity * pr.product.price
        amount+=val
    totalamount=amount
    return render(request,'ecommapp/addtocart.html',locals())

def plus_cart(request):
    if request.method=='GET':
        prod_id=request.GET.get('prod_id')
        c = Cart.objects.get(Q(product__id=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        cart=Cart.objects.filter(user=request.user)
        amount=0
        for p in cart:
            value=p.quantity * p.product.price
            amount+=value
        totalamount=amount
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount,
        }

    return JsonResponse(data)


def minus_cart(request):
    if request.method=='GET':
        prod_id=request.GET.get('prod_id')
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        cart=Cart.objects.filter(user=request.user)
        amount=0
        for p in cart:
            val=p.quantity * p.product.price
            amount+=val
        totalamount=amount
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount,
        }
    return JsonResponse(data)

def remove_cart(request):
    if request.method=='GET':
        prod_id=request.GET.get('prod_id')
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        
        cart=Cart.objects.filter(user=request.user)
        amount=0
        for p in cart:
            val=p.quantity * p.product.price
            amount+=val
        totalamount=amount
        data={
            'amount':amount,
            'totalamount':totalamount,
        }
    return JsonResponse(data)

def checkout(request):
    add=Customer.objects.filter(user=request.user)
    cart_items=Cart.objects.filter(user=request.user)
    amount=0
    for p in cart_items:
        val=p.quantity * p.product.price
        amount+=val
    totalamount=amount

    razoramount=int(totalamount * 100)

    client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

    data = { "amount": razoramount, "currency": "INR", "receipt": "order_rcptid_11" }
    payment_response = client.order.create(data=data)
    print(payment_response)
    #{'id': 'order_MIjRRkBjYiXtrP', 'entity': 'order', 'amount': 45600, 'amount_paid': 0, 'amount_due': 45600, 'currency': 'INR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1690440457}

    order_status=payment_response['status']
    if order_status == 'created':
        payment=Payment.objects.create(
            user=request.user,
            amount=totalamount,
            razorpay_order_id=payment_response['id'],
            razorpay_payment_status=order_status

        )
        payment.save()

    return render(request,'ecommapp/checkout.html',locals())


def payment_completed(request):
    
    order_id=request.GET.get('order_id')
    payment_id=request.GET.get('payment_id')
    cust_id=request.GET.get('cust_id')
    print(order_id,payment_id,cust_id)
    
    payment = Payment.objects.get(razorpay_order_id=order_id)
    payment.razorpay_payment_id=payment_id
    payment.paid=True
    payment.save()

    #for order
    cust=Customer.objects.get(id=cust_id)

    cart=Cart.objects.filter(user=request.user)
    for c in cart:
        OrderPlaced.objects.create(
            user=request.user,
            customer=cust,
            product=c.product,
            quantity=c.quantity,
            payment=payment,
        )
        c.delete()
    return redirect('orders') 

def orders(request):
    pass

    return render(request,'ecommapp/orders.html')


