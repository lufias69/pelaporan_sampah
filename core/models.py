from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    alamat = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
