from django import forms

from page.models import Fidelik, Urun,KATEGORI,CINS

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control form-control-user',
                'placeholder': 'Kullanıcı Adı'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control form-control-user',
                'placeholder':'Şifre'
            }
        )
    )


class NotForm(forms.Form):
    konu = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control'
            }
        )
    )


class FidelikForm(forms.ModelForm):
    isim = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control my-1',
                'placeholder':'Fidelik İsmi'
            }
        )
    )
    yetkili = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control my-1',
                'placeholder':'Yetkili İsmi'
            }
        )
    )
    tel = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control my-1',
                'placeholder':'Telefon Numarası'
            }
        )
    )
    mail = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control my-1',
                'placeholder':'Mail'
            }
        )
    )
    adres = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control my-1',
                'placeholder':'Adres'
            }
        )
    )
    mak_sayisi = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control my-1',
                'placeholder':'Makina Sayısı'
            }
        )
    )
    karistirici = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control my-1',
                'placeholder':'Karıştırıcı'
            }
        )
    )
    viyoller = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control my-1',
                'placeholder':'Viyoller'
            }
        )
    )
    makine = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control my-1',
                'placeholder':'Makina'
            }
        )
    )

    class Meta:
        model = Fidelik
        fields = ['makine','viyoller','karistirici','mak_sayisi','adres','mail','tel','yetkili','isim']



class UrunForm(forms.ModelForm):
    isim = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control my-1',
            'placeholder':'İsim'}
        )
    )
    kategori = forms.ChoiceField(
        choices=KATEGORI,
        widget=forms.Select(
            attrs={'class':'form-control my-1',
            'placeholder':'Kategori'}
        )
    )
    fiyat = forms.CharField(
        widget=forms.NumberInput(
            attrs={'class':'form-control my-1',
            'placeholder':'Fiyat'}
        )
    )
    cins =forms.ChoiceField(
        choices=CINS,
        widget=forms.Select(
            attrs={'class':'form-control my-1',
            'placeholder':'Cins'}
        )
    )



    class Meta:
        model = Urun
        fields = [
          "isim","kategori","fiyat",'cins'
        ]

