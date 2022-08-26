from django.contrib import admin
from django.urls import path
from django.urls import include, path

urlpatterns = [
    path('polls/', include('encuesta.urls')),
    path('operaciones/',include('operaciones.urls')),
    path('admin/', admin.site.urls),
]
