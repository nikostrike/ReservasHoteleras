"""
URL configuration for ReservaHotelera project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from core import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_view, name='landing'),
    path('habitaciones/', views.habitaciones, name='habitaciones'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('search/', views.search_rooms, name='search_rooms'),
    path('reservation/<int:habitacion_id>/', views.make_reservation, name='make_reservation'),
    path('mis-reservas/', views.mis_reservas, name='mis_reservas'),
    path('search/', views.search_rooms, name='search_rooms'),
]