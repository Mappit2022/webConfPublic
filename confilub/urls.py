from django.urls import path, reverse
from .views import *

urlpatterns = [
    path('', home, name = 'index'),
    path('Conocenos', conocenos, name = 'Conocenos'),
    path('Aprendizaje', aprendizaje, name = 'Aprendizaje'),
    path('Contacto', contacto, name = 'Contacto'),
    #servicios Core
    path('Diagnostico_campo', diagCamp, name = 'Diagnostico_campo'),
    path('BELUS', belus, name = 'BELUS'),
    path('Programas_descritos', programDes, name = 'Programas_descritos'),
    path('Procesos_filtracion', pfa, name = 'Procesos_filtracion'),
    path('Suministro_accesorios', sac, name = 'Suministro_accesorios'),
    path('Importancia_lubricacion', impLub, name = 'Importancia_lubricacion'),
]