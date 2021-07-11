"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views
# Urls administrativo
urlpatterns = [
        path('', views.index, name='index'),
        # Urls Edificio
        path('edificio/<int:id>', views.obtenerEdificio, 
            name='obtenerEdificio'),
        path('agregar/edificio', views.agregarEdificio, 
            name='agregarEdificio'),
        path('editarEdificio/<int:id>', views.editarEdificio, 
            name='editarEdificio'),
        path('eliminar/edificio/<int:id>', views.eliminarEdificio, 
            name='eliminarEdificio'),
        # Urls Departamento
        path('agregar/departamento', views.agregarDepartamento, 
            name='agregarDepartamento'),
        path('editar/departamento/<int:id>', views.editarDepartamento, 
            name='editarDepartamento'),
        path('eliminar/departamento/<int:id>', views.eliminarDepartamento, 
            name='eliminarDepartamento'),
        # Urls Departamento
        path('agregar/departamento/edificio/<int:id>', views.agregarDepartamentoEdificio, 
            name='agregarDepartamentoEdificio'),
      
 ]
