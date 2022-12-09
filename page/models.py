from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


KATEGORI=[
    ('Ayrıkmak Yedek Parçaları','Ayrıkmak Yedek Parçaları'),
    ("İthal Markalar Yedek Parçaları","İthal Markalar Yedek Parçaları"),
    ("Ayrıkmak Makinalar","Ayrıkmak Makinalar")
    ]

CINS=[
    ('dolar','$'),
    ("tl","₺"),
    ]


class Fidelik(models.Model):
    isim = models.CharField(max_length=200,null=True,blank=True)
    yetkili = models.CharField(max_length=200,null=True,blank=True)
    tel = models.CharField(max_length=11,null=True,blank=True)
    mail = models.CharField(max_length=200,null=True,blank=True)
    adres = models.CharField(max_length=200,null=True,blank=True)
    mak_sayisi = models.PositiveIntegerField(default=0,null=True,blank=True)
    karistirici = models.CharField(max_length=100,null=True,blank=True)
    makine = models.CharField(max_length=200,null=True,blank=True)
    viyoller = models.CharField(max_length=500,null=True,blank=True)




class Urun(models.Model):
    isim = models.CharField(max_length=200,null=True,blank=True)
    kategori = models.CharField(choices=KATEGORI,max_length=200,null=True,blank=True)
    fiyat = models.PositiveBigIntegerField(null=True,blank=True)
    tarih = models.DateField(auto_now=True)
    cins = models.CharField(choices=CINS,max_length=200,null=True)


class Not(models.Model):
    fidelik = models.ForeignKey(Fidelik, on_delete=models.CASCADE)
    konu = models.TextField()
    tarih = models.DateField(auto_now_add=True)


class Notification(models.Model):
    baslik = models.CharField(max_length=50)
    fidelik = models.ForeignKey(Fidelik,on_delete=models.SET_NULL,null=True)
    alici = models.ForeignKey(User,on_delete=models.CASCADE)
    goruldu = models.BooleanField(default=False)
    tarih = models.DateTimeField(auto_now=True)




@receiver(post_save, sender=Not)
def shopping_cart_item_receiver(sender, created,instance,*args, **kwargs):
    users = User.objects.all()
    if created:
        for i in users:
           a = Notification(baslik="{} isimli fideliğe bir not eklendi.".format(instance.fidelik.isim),alici = i,goruldu=False,fidelik=instance.fidelik)
           a.save()
    
