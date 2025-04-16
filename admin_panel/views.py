from django.shortcuts import render
from laporan.models import Laporan

def admin_dashboard(request):
    laporan_list = Laporan.objects.all()
    return render(request, 'admin_panel/admin_dashboard.html', {'laporan_list': laporan_list})
