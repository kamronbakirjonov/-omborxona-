from django.db.models.fields import return_None
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from datetime import datetime

from stats.models import Sotuv
from .models import *


class BolimView(View):
    def get(self, request):
        if request.user.is_authenticated and not request.user.is_superuser:
            return render(request, "bo'limlar.html")
        return redirect('login')


class MahsulotlarViews(View):
    def get(self, request, ):
        if request.user.is_authenticated and not request.user.is_superuser:
            mahsulotlar = Mahsulot.objects.filter(bolim=request.user.xodim.bolim)
            context = {
                'mahsulotlar': mahsulotlar,
                'bugun': datetime.today(),
            }
            return render(request, 'mahsulotlar.html', context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            narx2 = float(request.POST.get('narx2'))
            if narx2 == '':
                narx2 = None
            Mahsulot.objects.create(
                nom=request.POST.get('nom'),
                brend=request.POST.get('brend'),
                narx1=request.POST.get('narx1'),
                narx2=narx2,
                miqdor=request.POST.get('miqdor'),
                olchov=request.POST.get('olchov'),
                sana=request.POST.get('sana'),
                bolim=get_object_or_404(Bolim, id=1),
            )
            return redirect('mahsulotlar')
        return redirect('login')


class MahsulotTahrirlashViews(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = get_object_or_404(Mahsulot, id=pk, bolim=request.user.xodim.bolim)
            context = {
                'mahsulot': mahsulot,
            }
            return render(request, 'mahsulot-tahrirlash.html', context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            narx2 = request.POST.get('narx2'),
            if narx2 == '':
                narx2 = None
            Mahsulot.objects.update(
                nom=request.POST.get('nom'),
                brend=request.POST.get('brend'),
                narx1=request.POST.get('narx1'),
                narx2=narx2,
                miqdor=request.POST.get('miqdor'),
                olchov=request.POST.get('olchov'),
                sana=datetime.today(),
                bolim=request.user.xodim.bolim
            )
            return redirect('mahsulotlar')
        return redirect('login')


class MahsulotOchirishViews(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = get_object_or_404(Mahsulot, id=pk, bolim=request.user.xodim.bolim)
            context = {
                'mahsulot': mahsulot,
            }
            return render(request, "mahsulot-o'chirish.html", context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = get_object_or_404(Mahsulot, id=pk, bolim=request.user.xodim.bolim)
            mahsulot.delete()
            return redirect('mahsulotlar')
        return redirect('login')


class MijozlarViews(View):
    def get(self, request):
        if request.user.is_authenticated:
            mijozlar = Mijoz.objects.all()
            context = {
                'mijozlar': mijozlar,

            }
            return render(request, 'mijozlar.html', context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Mijoz.objects.create(
                ism=request.POST.get('ism'),
                dokon=request.POST.get('dokon'),
                tel=request.POST.get('tel'),
                manzil=request.POST.get('manzil'),
                qarz=request.POST.get('qarz'),
                bolim=get_object_or_404(Bolim, id=1),
            )
            return redirect('mijozlar')
        return redirect('login')


class MijozTahrirlashViews(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mijoz = get_object_or_404(Mijoz, id=pk, bolim=request.user.xodim.bolim)
            context = {
                'mijoz': mijoz,
            }
            return render(request, 'mijoz-tahrirlash.html', context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            Mijoz.objects.update(
                nom=request.POST.get('nom'),
                dokon=request.POST.get('dokon'),
                tel=request.POST.get('tel'),
                manzil=request.POST.get('manzil'),
                qarz=request.POST.get('qarz'),

            )
            return redirect('mijozlar')
        return redirect('login')


class MijozOchirishViews(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mijozlar = get_object_or_404(Mahsulot, id=pk, bolim=request.user.xodim.bolim)
            context = {
                'mijozlar': mijozlar,
            }
            return render(request, "mijozlar-o'chirish.html", context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            mijozlar = get_object_or_404(Mahsulot, id=pk, bolim=request.user.xodim.bolim)
            mijozlar.delete()
            return redirect('mijozlar')
        return redirect('login')
