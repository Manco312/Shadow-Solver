from django.urls import path
from . import views

urlpatterns = [
    path('options/', views.optionsch1, name ='optionsch1'),
    path('biseccion/', views.biseccion_view, name ='biseccion'),
    path('reglafalsa/', views.regla_falsa_view, name ='reglafalsa'),
    path('puntofijo/', views.punto_fijo_view, name ='puntofijo'),
    path('newton/', views.newton_view, name ='newton'),
    path('secante/', views.secante_view, name ='secante'),
    path('raicesmultiples/', views.raices_multiples_view, name ='raicesmultiples'),
]