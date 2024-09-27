from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Hotel, Habitacion, Reserva
from django.db.models import Q
from datetime import datetime
from django.core.exceptions import ValidationError

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def search_rooms(request):
    if request.method == 'POST':
        fecha_llegada = request.POST.get('fecha_llegada')
        fecha_salida = request.POST.get('fecha_salida')
        
        # Validación de fechas
        try:
            fecha_llegada = datetime.strptime(fecha_llegada, '%Y-%m-%d').date()
            fecha_salida = datetime.strptime(fecha_salida, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'error.html', {'message': 'Formato de fecha inválido. Use YYYY-MM-DD.'})
        
        if fecha_llegada >= fecha_salida:
            return render(request, 'error.html', {'message': 'La fecha de llegada debe ser anterior a la fecha de salida.'})
        
        # Buscar habitaciones disponibles
        habitaciones_disponibles = Habitacion.objects.exclude(
            reserva__fecha_inicio__lt=fecha_salida,
            reserva__fecha_fin__gt=fecha_llegada
        )
        
        return render(request, 'habitaciones_disponibles.html', {
            'habitaciones': habitaciones_disponibles,
            'fecha_llegada': fecha_llegada,
            'fecha_salida': fecha_salida
        })
    
    return render(request, 'search_rooms.html')

@login_required
def make_reservation(request, habitacion_id):
    if request.method == 'POST':
        habitacion = get_object_or_404(Habitacion, id_habitacion=habitacion_id)
        fecha_llegada = request.POST.get('fecha_llegada')
        fecha_salida = request.POST.get('fecha_salida')
        
        if not fecha_llegada or not fecha_salida:
            return render(request, 'error.html', {'message': 'Las fechas son requeridas'})
        
        try:
            fecha_llegada = datetime.strptime(fecha_llegada, '%Y-%m-%d').date()
            fecha_salida = datetime.strptime(fecha_salida, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'error.html', {'message': 'Formato de fecha inválido. Use YYYY-MM-DD.'})
        
        try:
            # Crear la reserva
            reserva = Reserva.objects.create(
                id_usuario_usuario=request.user,
                id_habitacion_habitacion=habitacion,
                fecha_inicio=fecha_llegada,
                fecha_fin=fecha_salida,
                precio_total=habitacion.precio_base * (fecha_salida - fecha_llegada).days,
                estado='CONFIRMADA'
            )
            return redirect('mis_reservas')
        except ValidationError as e:
            return render(request, 'error.html', {'message': str(e)})
    
    return render(request, 'make_reservation.html', {'habitacion_id': habitacion_id})

@login_required
def mis_reservas(request):
    reservas = Reserva.objects.filter(id_usuario_usuario=request.user)
    return render(request, 'mis_reservas.html', {'reservas': reservas})