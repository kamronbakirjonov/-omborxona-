from django.db import models
from main.models import *

class Sotuv(models.Model):
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.SET_NULL,null=True)
    mijoz =models.ForeignKey(Mijoz,on_delete=models.SET_NULL,null=True)
    miqdor =models.FloatField()
    jami = models.FloatField()
    tolandi = models.FloatField(default=0)
    qarz = models.FloatField(default=0)
    sana = models.DateField(auto_now_add=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mahsulot}:{self.mijoz} "