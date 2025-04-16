# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
# from django.http import HttpResponse
# from .models import Profile
#
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             Profile.objects.create(user=user)  # Create an empty profile for the user
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'core/register.html', {'form': form})



# from django.contrib.auth.views import LoginView, LogoutView
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
#
# # Tidak perlu lagi mendefinisikan LoginView secara manual karena kita akan menggunakan Django's built-in view
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'core/register.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)  # Gunakan request.FILES untuk menangani file (foto)
        if form.is_valid():
            form.save()  # Menyimpan User dan Profile
            return redirect('login')  # Redirect ke halaman login setelah registrasi berhasil
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Menambahkan tampilan profil pengguna
# @login_required
# def profile(request):
#     return render(request, 'core/profile.html', {'user': request.user})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from laporan.models import Laporan
from laporan.forms import CustomUserCreationForm


@login_required (login_url='login')
def profile(request):
    # Menampilkan laporan yang telah diajukan oleh pengguna yang sedang login
    laporan_list = Laporan.objects.filter(user=request.user)

    # Jika pengguna ingin melaporkan masalah baru
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            laporan = form.save(commit=False)
            laporan.user = request.user  # Menyimpan laporan dengan pengguna yang sedang login
            laporan.save()
            return redirect('profile')  # Redirect ke halaman profil setelah berhasil melaporkan masalah
    else:
        form = CustomUserCreationForm()  # Form untuk melaporkan masalah baru

    return render(request, 'core/profile.html', {'user': request.user, 'laporan_list': laporan_list, 'form': form})
