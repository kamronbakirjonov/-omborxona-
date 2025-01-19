from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',SotuvlarViews.as_view(),name='sotuvlar'),
    path('<int:pk>/o\'chirish/ ',SotuvOchirishView.as_view()),
    path('<int:pk>/tahrirlash/', SotuvTahrirlashViews.as_view()),


]
