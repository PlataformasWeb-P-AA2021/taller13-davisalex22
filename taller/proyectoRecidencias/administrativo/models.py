from django.db import models

# Create your models here.


class Edificio(models.Model):
    class Meta:       
        verbose_name_plural = "Edificios"
    # Opciones atributo tipo edificio   
    opciones_tipo = (
    ('residencial','Residencial'),
    ('comercial','Comercial'),
    )
    nombre = models.CharField(max_length=600)
    direccion = models.CharField(max_length=60)
    ciudad = models.CharField(max_length=40, unique=True)
    tipo = models.CharField(max_length=30, \
            choices= opciones_tipo) 

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)
        
# Modelo entidad Departamento
class Departamento(models.Model):
    propietario = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=100, decimal_places=2)
    numCuartos = models.IntegerField("numero de cuartos")
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s %.2f %d %s" % (self.propietario,
                self.costo,
                self.numCuartos,
                self.edificio)
