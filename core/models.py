from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rut_cliente = models.CharField(max_length=13)
    nombre_cliente = models.CharField(max_length=50)
    apellido_cliente = models.CharField(max_length=50)
    telefono_cliente = models.CharField(max_length=14)

    def __str__(self):
        return f"{self.nombre_cliente} {self.apellido_cliente}"


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    rut_empleado = models.CharField(max_length=13)
    nombre_empleado = models.CharField(max_length=50)
    apellido_empleado = models.CharField(max_length=50)
    cargo = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f"{self.nombre_empleado} {self.apellido_empleado}"


class Hotel(models.Model):
    id_hotel = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    estrellas = models.IntegerField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Habitacion(models.Model):
    id_habitacion = models.AutoField(primary_key=True)
    id_hotel_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    numero_hab = models.IntegerField()
    categoria = models.CharField(max_length=30, choices=[('TURISTA', 'Turista'), ('PREMIUM', 'Premium')])
    capacidad = models.IntegerField()
    precio_base = models.FloatField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"Habitación {self.numero_hab} - {self.categoria}"


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    id_usuario_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_habitacion_habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio_total = models.FloatField()
    estado = models.CharField(max_length=20, choices=[('PENDIENTE', 'Pendiente'), ('CONFIRMADA', 'Confirmada'), ('CANCELADA', 'Cancelada')])

    def __str__(self):
        return f"Reserva {self.id_reserva} - {self.estado}"


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_reserva_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    monto = models.FloatField()
    fecha_pago = models.DateField()
    metodo = models.CharField(max_length=20, choices=[('TARJETA', 'Tarjeta'), ('TRANSFERENCIA', 'Transferencia'), ('EFECTIVO', 'Efectivo')])
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"Pago {self.id_pago} - {self.metodo}"


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    id_cliente_cliente = models.OneToOneField(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    id_empleado_empleado = models.OneToOneField(Empleado, on_delete=models.SET_NULL, null=True, blank=True)
    nombre_usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    email = models.EmailField()
    fecha_registro = models.DateField()
    tipo = models.CharField(max_length=30, choices=[('CLIENTE', 'Cliente'), ('EMPLEADO', 'Empleado'), ('ADMINISTRADOR', 'Administrador')])
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_usuario