from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Urun,Fidelik,Not,Notification
from .forms import LoginForm, NotForm,FidelikForm, UrunForm


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("mainpage")
    else:
        context = dict()
        context['title'] = "Giriş"
        if request.method == 'POST':
            context['form'] = LoginForm(request.POST)
            if context['form'].is_valid():
                username = context['form'].cleaned_data['username']
                password = context['form'].cleaned_data['password']
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        return redirect('mainpage')
                    else:
                        messages.info(request,'Engellendin')
                else:
                    messages.info(request,'Hatalı kullanıcı adı veya şifre')
        else:
            context['form'] = LoginForm()
        return render(request,"login.html",context)


def logoutPage(request):
    logout(request)
    return redirect("loginPage")


def mainpage(request):
    if request.user.is_authenticated:
        context = dict()
        context['title'] = "Anasayfa"
        fidelik = Fidelik.objects.all()
        urun = Urun.objects.all()
        context['fidelik'] = len(fidelik)
        context['urun'] = len(urun)
        return render(request,"main.html",context)
    else:
        return redirect("loginPage")


def machines(request):
    if request.user.is_authenticated:
        context = dict()
        context['title'] = "Makinalar"
        context['subtitle'] = "Ayrıkmak Ürünleri"
        category = "Ayrıkmak Makinalar"
        context['items'] = Urun.objects.filter(kategori=category)
        return render(request,"products_tables.html",context)
    else:
        return redirect("loginPage")


def native_products(request):
    if request.user.is_authenticated:
        context = dict()
        context['title'] = "Yedek Parçalar"
        context['subtitle'] = "Ayrıkmak Ürünleri Yedek Parçaları"
        category = "Ayrıkmak Yedek Parçaları"
        context['items'] = Urun.objects.filter(kategori=category)
        return render(request,"products_tables.html",context)
    else:
        return redirect("loginPage")


def products(request):
    if request.user.is_authenticated:
        context = dict()
        context['title'] = "İthal Markalar Yedek Parçaları"
        context['subtitle'] = "İthal Markalar Yedek Parçaları"
        category = "İthal Markalar Yedek Parçaları"
        context['items'] = Urun.objects.filter(kategori=category)
        return render(request,"products_tables.html",context)
    else:
        return redirect("loginPage")

def allPproducts(request):
    if request.user.is_authenticated:
        context = dict()
        context['title'] = "Tüm Ürünler"
        context['subtitle'] = "Tüm ürünler"
        context['items'] = Urun.objects.all()
        return render(request,"all_products.html",context)
    else:
        return redirect("loginPage")


def customers(request):
    if request.user.is_authenticated:
        context = dict()
        context['title'] = "Fidelikler"
        context['items'] = Fidelik.objects.all()
        return render(request,"customers_tables.html",context)
    else:
        return redirect("loginPage")


def references(request):
    if request.user.is_authenticated:
        context = dict()
        context['title'] = "Müşterilerimiz"
        fidelikler = Fidelik.objects.all()
        context['items'] = list()
        for item in fidelikler:
            if item.makine == "Ayrıkmak":
                context['items'].append(item)
            elif item.karistirici == "Ayrıkmak":
                context['items'].append(item)
        return render(request,"customers_tables.html",context)
    else:
        return redirect("loginPage")


def customer_detail(request,customer_pk):
    if request.user.is_authenticated:
        context = dict()
        fidelik = Fidelik.objects.get(pk=customer_pk)
        context['fidelik'] = Fidelik.objects.get(pk=customer_pk)
        context['title'] = Fidelik.objects.get(pk=customer_pk).isim
        context['nots'] = Not.objects.filter(fidelik=fidelik).order_by("-pk")
        context['form'] = NotForm(request.POST)
        if request.method == 'POST':
            if context['form'].is_valid():
                konu = context['form'].cleaned_data['konu']
                a = Not(fidelik=context['fidelik'],konu=konu)
                a.save()
                return redirect('customer_detail',customer_pk=customer_pk)
        return render(request, "customer_detail.html",context)
    else:
        return redirect("loginPage")


def customer_redirect(request,notification_pk):
    if request.user.is_authenticated:
        context = dict()
        bildirim = Notification.objects.get(pk=notification_pk)
        bildirim.goruldu = True
        bildirim.save()
        fidelik = Fidelik.objects.get(pk=bildirim.fidelik.pk)
        context['fidelik'] = Fidelik.objects.get(pk=bildirim.fidelik.pk)
        context['title'] = Fidelik.objects.get(pk=bildirim.fidelik.pk).isim
        context['nots'] = Not.objects.filter(fidelik=fidelik).order_by("-pk")
        context['form'] = NotForm(request.POST)
        if request.method == 'POST':
            if context['form'].is_valid():
                konu = context['form'].cleaned_data['konu']
                a = Not(fidelik=context['fidelik'],konu=konu)
                a.save()
                return redirect('customer_detail',customer_pk=bildirim.fidelik.pk)
        return render(request, "customer_detail.html",context)
    else:
        return redirect("loginPage")


def addCustomer(request):
    if request.user.is_authenticated:
        context = dict()
        context['title'] = "Fidelik Ekle"
        context['form'] = FidelikForm(request.POST)
        if request.method == "POST":
            if context['form'].is_valid():
                context['form'].save()
                messages.success(request,'Fidelik Başarıyla Eklendi..')
                return redirect("customers")                
        return render(request,"fidelik_form.html",context)
    else:
        return redirect("loginPage")


def changeCustomer(request,customer_pk):
    if request.user.is_authenticated:
        context = dict()
        context['title'] = "Fideliği Düzenle"
        customer = Fidelik.objects.get(pk=customer_pk)
        context['customer'] = customer
        context['form'] = FidelikForm(instance=customer)
        if request.method == "POST":
            context['form'] = FidelikForm(request.POST,request.FILES,instance=customer)
            if context['form'].is_valid():
                item = context['form'].save(commit=False)
                item.save()
                messages.success(request,'Fidelik Başarıyla Kaydedildi')            
                return redirect('customer_detail',customer_pk=customer_pk)                
        return render(request,"fidelik_form.html",context)
    else:
        return redirect("loginPage")


def addProduct(request):
    if request.user.is_authenticated:
        context = dict()
        context['title'] = "Ürün Ekle"
        context['form'] = UrunForm(request.POST)
        if request.method == "POST":
            if context['form'].is_valid():
                context['form'].save()
                messages.success(request,'Ürün Başarıyla Eklendi..')
                return redirect("mainpage")                
        return render(request,"products_form.html",context)
    else:
        return redirect("loginPage")


def changeProduct(request,product_pk):
    if request.user.is_authenticated:
        context = dict()        
        product = Urun.objects.get(pk=product_pk)
        context['product'] = product
        context['title'] = "Ürünü Güncelle"
        context['form'] = UrunForm(instance=product)
        if request.method == "POST":
            context['form'] = UrunForm(request.POST,request.FILES,instance=product)
            if context['form'].is_valid():
                item = context['form'].save(commit=False)
                item.save()
                return redirect("allPproducts")                
        return render(request,"products_form.html",context)
    else:
        return redirect("loginPage")


def deleteProduct(request,product_pk):
    product = Urun.objects.get(pk=product_pk)
    product.delete()
    messages.warning(request,'Ürün Başarıyla Silindi..')
    return redirect('allPproducts')


def deleteCustomer(request,customer_pk):
    fidelik = Fidelik.objects.get(pk=customer_pk)
    fidelik.delete()
    messages.info(request,'Fidelik Başarıyla Silindi..')
    return redirect('customers')

def deleteNotification(request):
    user = User.objects.get(pk=request.user.pk)
    notification = Notification.objects.filter(alici=user,goruldu=True)
    for item in notification:
        item.delete()
    return redirect('mainpage')

def deleteNot(request,not_pk):
    item = Not.objects.get(pk=not_pk)
    fidelik = item.fidelik
    item.delete()
    messages.info(request,'Not Başarıyla Silindi..')
    return redirect('customer_detail' ,customer_pk=fidelik.pk)


