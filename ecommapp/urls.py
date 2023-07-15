from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('categories/<str:pk>/',views.categories,name='categories'),
    path('product-detail/<str:pk>/',views.productDetail,name='product-detail')
]