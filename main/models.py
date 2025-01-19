from django.db import models
from django.core.validators import MinValueValidator

class Bolim(models.Model):
    nom = models.CharField(max_length=100)

    def _str_(self):
        return self.nom
class Mahsulot(models.Model):
    nom = models.CharField(max_length=100)
    brend =models.CharField(max_length=255)
    narx1 = models.FloatField(validators=[MinValueValidator(0)])
    narx2 = models.FloatField(validators=[MinValueValidator(0)])
    miqdor = models.FloatField()
    olchov = models.CharField(max_length=255)
    sana = models.DateField()
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)

    def _str_(self):
        return self.nom

class Mijoz(models.Model):
    ism = models.CharField(max_length=255)
    dokon = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    manzil = models.TextField(blank=True,null=True)
    qarz = models.FloatField(default=0)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)


    def _str_(self):
        return self.ism
