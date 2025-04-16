from django.shortcuts import render, redirect
from .models import Pengangkutan
from laporan.models import Laporan
from .forms import PengangkutanForm

# def pengelola_dashboard(request):
#     laporan_list = Laporan.objects.all()
#     return render(request, 'pengelola/pengelola_dashboard.html', {'laporan_list': laporan_list})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Pengangkutan
from laporan.models import Laporan

# Fungsi untuk memastikan hanya petugas atau admin yang bisa mengakses
def is_pengelola(user):
    return user.is_authenticated and user.is_staff  # Cek apakah pengguna adalah staff (admin atau petugas)

@login_required
@user_passes_test(is_pengelola)  # Pastikan hanya petugas atau admin yang bisa mengakses
def pengelola_dashboard(request):
    laporan_list = Laporan.objects.all()  # Menampilkan semua laporan
    return render(request, 'pengelola/pengelola_dashboard.html', {'laporan_list': laporan_list})



def tanggapi_laporan(request, id):
    laporan = Laporan.objects.get(id=id)
    laporan.status = 'diproses'
    laporan.save()
    return redirect('pengelola_dashboard')
