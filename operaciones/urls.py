from django.urls import path

from . import views

urlpatterns = [
    # ex: localhost:8000/polls/
    path('', views.index, name='index'),
    # ex: localhost:8000/app/sumar/18/19/
    path('sumar/<int:n1>/<int:n2>/', views.suma, name='sumar'),
    # ex: localhost:8000/app/restar/18/19/
    path('restar/<int:n1>/<int:n2>/', views.resta, name='restar'),
    # ex: localhost:8000/app/multiplicar/18/19/
    path('multiplicar/<int:n1>/<int:n2>/', views.multiplicacion, name='multiplicar'),
]