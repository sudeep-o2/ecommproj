from django.contrib import admin
from django.urls import path
from . import views
from . forms import MyPasswordChangeForm
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.aboutus,name='about'),
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('register/',views.register,name='register'),
    path('categories/<str:pk>/',views.categories,name='categories'),
    path('product-detail/<str:pk>/',views.productDetail,name='product-detail'),
    path('products/',views.product_filter,name='productfilter'),
    path('profile/',views.profile,name='profile'),
    path('adress/',views.adress,name='adress'),
    path('updateadress/<str:pk>/',views.updateAdress,name='updateadress'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.show_cart,name='cart'),

    path('pluscart/',views.plus_cart,name='pluscart'),
    path('minuscart/',views.minus_cart,name='minuscart'),
    path('removecart/',views.remove_cart,name='removecart'),

    path('wishlist',views.wish_list,name='wishlist'),

    path('pluswishlist/',views.plus_wishlist,name='pluswishlist'),
    path('minuswishlist/',views.minus_wishlist,name='minuswishlist'),

    path('checkout/',views.checkout,name='checkout'),
    path('paymentcompleted/',views.payment_completed,name='paymentcompleted'),
    path('orders/',views.orders,name='orders'),
    
    

    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='ecommapp/changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='ecommapp/passwordchangedone.html'),name='passwordchangedone'),
]