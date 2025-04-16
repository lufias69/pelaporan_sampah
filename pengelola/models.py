from django.db import models
from django.contrib.auth.models import User

class Pengangkutan(models.Model):
    tanggal = models.DateTimeField()
    lokasi = models.CharField(max_length=255)
    petugas = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Pengangkutan pada {self.tanggal} di {self.lokasi}"
