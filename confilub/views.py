from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings

from_correo = settings.EMAIL_HOST_USER

# Inicio o index
def home(request):
    return render(request, 'index.html')

#navegacion de la pagina
def conocenos(request):
    return render(request, 'conocenos.html')

def aprendizaje(request):
    return render(request, 'aprendizaje.html')

def contacto(request):
    return render(request, 'contacto.html')

#Servicios Core
def diagCamp(request):
    return render(request, 'diagnostico_campo.html')

def belus(request):
    return render(request, 'belus.html')

def programDes(request):
    return render(request, 'programas_descritos.html')

def pfa(request):
    return render(request, 'pfa.html')

def sac(request):
    return render(request, 'sac.html')

def impLub(request):
    return render(request, 'importancia_lub.html')