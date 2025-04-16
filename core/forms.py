from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    foto = forms.ImageField(required=False)  # Menambahkan field foto
    alamat = forms.CharField(max_length=255, required=False)  # Menambahkan field alamat

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('foto', 'alamat')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        # Menyimpan Profile pengguna
        profile = Profile(user=user, foto=self.cleaned_data.get('foto'), alamat=self.cleaned_data.get('alamat'))
        profile.save()
        return user
