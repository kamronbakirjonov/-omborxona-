from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    path('',BolimView.as_view(),name='home'),
    path('mahsulotlar/',MahsulotlarViews.as_view(),name='mahsulotlar'),
    path('mahsulotlar/<int:pk>/tahrirlash/',MahsulotTahrirlashViews.as_view(),name='tahrirlash'),
    path("mahsulotlar/<int:pk>/o'chirish/", MahsulotOchirishViews.as_view(), name="o'chirish"),
    path('mijozlar/', MijozlarViews.as_view(), name='mijozlar'),
    path('mijozlar/<int:pk>/tahrirlash/',MijozTahrirlashViews.as_view(),name='tahrirlash'),
    path("mijozlar/<int:pk>/o'chirish/",MijozOchirishViews.as_view(),name="o'chirish"),

]
