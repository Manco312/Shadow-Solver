from django.urls import path
from . import views

urlpatterns = [
    path('options/', views.optionsch1, name ='optionsch1'),
]