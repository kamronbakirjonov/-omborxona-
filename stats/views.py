from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.views import View
from datetime import datetime




class SotuvlarViews(View):
    def get(self, request):
        sotuvlar = Sotuv.objects.all()
        mahsulot = Mahsulot.objects.all()
        mijozlar = Mijoz.objects.all()
        context ={
            'sotuvlar': sotuvlar,
            'mahsulot': mahsulot,
            'mijozlar': mijozlar,
            'hozir': datetime.now(),
        }
        return render(request, 'sotuvlar.html', context)
    def post(self, request):
        mahsulot = get_object_or_404(Mahsulot, id=request.POST.get('mahsulot_id'))
        mijoz_id = get_object_or_404(Mijoz, request.POST.get('mijoz_id'))
        qarz = request.POST.get('qarz')
        tolandi = request.POST.get('tolandi')
        jami = request.POST.get('jami')
        miqdor = float(request.POST.get('miqdor'))

        if miqdor > mahsulot.miqdor:
            return render(request,'error.html', {'xatolik':"Omborda mahsulot yetarli emas!" })
        if jami is None or jami == '':
            jami = mahsulot.narx2 * miqdor
        else:
            jami = float(jami)
        if bool(tolandi) and bool(qarz):
            if tolandi + qarz  == jami:
                return render(request,'error.html', {'xatolik':"Qarz ve tolandi bir-birine esas edilmelidir!" })
        if qarz is None or qarz == '':
            qarz = jami
        else:
            qarz = float(qarz)

        if tolandi is None or tolandi == '':
           tolandi = jami - qarz
        else:
            tolandi = float(tolandi)
            qarz = jami - tolandi

        Sotuv.objects.create(
            mahsulot_id = mahsulot,
            mijoz_id = mijoz_id,
            sana = request.POST.get('sana'),
            miqdor = request.POST.get('miqdor'),
            jami = jami,
            qarz = qarz,
            tolandi = tolandi,
            bolim=get_object_or_404(Bolim,id=1)
        )
        mahsulot.miqdor -= miqdor
        mahsulot.save()
        mijoz_id.qarz += qarz
        mijoz_id.save()
        return redirect('sotuvlar')
class  SotuvOchirishView(View):
    def get(self, request, pk):
        sotuv = get_object_or_404(Sotuv, id=pk)
        context ={
            'sotuv': sotuv,
        }
        return render(request,'sotuv-o\'chirish.html',context)
    def post(self,request,pk):
        sotuv = get_object_or_404(Sotuv, id=pk)
        mahsulot = sotuv.mahsulot
        mahsulot.miqdor += sotuv.miqdor
        mahsulot.save()

        mijoz = sotuv.mijoz
        mijoz.qarz -= sotuv.qarz
        mijoz.save()

        sotuv.delete()
        return redirect('sotuvlar')
class SotuvTahrirlashViews(View):
    def get(self,request, pk):
        sotuv = get_object_or_404(Mijoz, id=pk)
        mahsulot = Mahsulot.objects.all()
        mijoz = Mijoz.objects.all()
        context = {
            'sotuv': sotuv,
            'mahsulot': mahsulot,
            'mijoz': mijoz,
        }
        return render(request, 'sotuv-tahrirlash.html', context)
    def post(self, request, pk):
        sotuvlar = Sotuv.objects.filter(id=pk)
        if sotuvlar.exists():
            mahsulot = get_object_or_404(Mahsulot, id=request.POST.get('mahsulot_id'))
            mijoz = get_object_or_404(Mijoz, id=request.POST.get('mijoz_id'))
            sotuvlar.updeta(
                mahsulot_id = mahsulot,
                mijoz_id = mijoz,
                sana = request.POST.get('sana'),
                miqdor = request.POST.get('miqdor'),
                jami = request.POST.get('jami'),
                qarz = request.POST.get('qarz'),
                tolandi = request.POST.get('tolandi'),
            )
            return redirect('sotuvlar')