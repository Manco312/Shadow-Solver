from django.urls import path
from . import views

urlpatterns = [
    path('options/', views.optionsch1, name ='optionsch1'),
    path('biseccion/', views.biseccion_view, name ='biseccion'),
]