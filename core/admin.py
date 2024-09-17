from django.contrib import admin
from .models import Cliente, Empleado, Hotel, Habitacion, Reserva, Pago, Usuario

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'rut_cliente', 'nombre_cliente', 'apellido_cliente', 'telefono_cliente')
    search_fields = ('nombre_cliente', 'apellido_cliente')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'rut_empleado', 'nombre_empleado', 'apellido_empleado', 'cargo', 'fecha_contratacion')
    search_fields = ('nombre_empleado', 'apellido_empleado', 'cargo')

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

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('id_pago', 'id_reserva_reserva', 'monto', 'fecha_pago', 'metodo', 'estado')
    list_filter = ('metodo',)
    search_fields = ('estado',)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'id_cliente_cliente', 'id_empleado_empleado', 'nombre_usuario', 'email', 'fecha_registro', 'tipo', 'activo')
    list_filter = ('tipo', 'activo')
    search_fields = ('nombre_usuario', 'email')
