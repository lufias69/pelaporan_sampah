from django.urls import path
from . import views

urlpatterns = [
    # path('pengelola/', views.pengelola_dashboard, name='pengelola_dashboard'),
    path('pengelola/laporan/<int:id>/', views.tanggapi_laporan, name='tanggapi_laporan'),
    path('laporan/<int:id>/', views.tanggapi_laporan, name='tanggapi_laporan'),

    path('', views.pengelola_dashboard, name='pengelola_dashboard'),
]
