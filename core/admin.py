from django.contrib import admin
from .models import Hotel, Habitacion, Reserva

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id_hotel', 'nombre', 'direccion', 'estrellas', 'descripcion')
    search_fields = ('nombre', 'direccion')

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('id_habitacion', 'id_hotel_hotel', 'numero_hab', 'categoria', 'capacidad', 'precio_base', 'descripcion')
    list_filter = ('categoria',)
    search_fields = ('descripcion', 'numero_hab')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id_reserva', 'id_usuario_usuario', 'id_habitacion_habitacion', 'fecha_inicio', 'fecha_fin', 'precio_total', 'estado')
    list_filter = ('estado',)
    search_fields = ('id_reserva',)