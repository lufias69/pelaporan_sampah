from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # URL untuk halaman registrasi
    # path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),  # Menggunakan LoginView dari Django
    path('logout/', LogoutView.as_view(), name='logout'),  # Menggunakan LogoutView dari Django
    path('profile/', views.profile, name='profile'),
]
