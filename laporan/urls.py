from django.urls import path
from . import views

urlpatterns = [
    # path('laporan/', views.laporan, name='laporan'),
    path('status/', views.status_laporan, name='status_laporan'),

    path('', views.laporan, name='laporan'),  # URL untuk membuat laporan masalah sampah
    path('status/', views.status_laporan, name='status_laporan'),  # URL untuk melihat status laporan

]
