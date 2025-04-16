from django.shortcuts import render, redirect
from .models import Laporan
from .forms import CustomUserCreationForm as LaporanForm

def laporan(request):
    if request.method == 'POST':
        form = LaporanForm(request.POST, request.FILES)
        if form.is_valid():
            laporan = form.save(commit=False)
            laporan.user = request.user
            laporan.save()
            return redirect('status_laporan')
    else:
        form = LaporanForm()
    return render(request, 'laporan/laporan.html', {'form': form})

def status_laporan(request):
    laporan_list = Laporan.objects.filter(user=request.user)
    return render(request, 'laporan/status_laporan.html', {'laporan_list': laporan_list})
