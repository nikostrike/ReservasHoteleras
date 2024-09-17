from django.shortcuts import render

# Create your views here.
def home(request):
    ''' Vista para renderizar el home '''
    return render(request, 'home.html')