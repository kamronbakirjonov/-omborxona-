from django.db import models
from django.contrib.auth.models import User
from main.models import Bolim


class Xodim(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='xodimlar/', blank=True, null=True)

    def __str__(self):
        return self.user.username