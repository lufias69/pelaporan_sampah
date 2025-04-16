from django import forms
from .models import Pengangkutan

class PengangkutanForm(forms.ModelForm):
    class Meta:
        model = Pengangkutan
        fields = ['tanggal', 'lokasi', 'status']
