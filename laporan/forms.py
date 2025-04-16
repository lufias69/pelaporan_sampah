# from django import forms
# from .models import Laporan
#
# class LaporanForm(forms.ModelForm):
#     class Meta:
#         model = Laporan
#         fields = ['judul', 'deskripsi', 'lokasi', 'foto']


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    foto = forms.ImageField(required=False)  # Menambahkan field foto
    alamat = forms.CharField(max_length=255, required=False)  # Menambahkan field alamat

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Menambahkan kelas CSS untuk setiap field form
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['foto'].widget.attrs.update({'class': 'form-control'})
        self.fields['alamat'].widget.attrs.update({'class': 'form-control'})

