from django.db import models
from django.contrib.auth.models import User

class Laporan(models.Model):
    STATUS_CHOICES = [
        ('menunggu', 'Menunggu'),
        ('diproses', 'Diproses'),
        ('selesai', 'Selesai'),
    ]
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    lokasi = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='laporan_pics/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='menunggu')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal_laporan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
