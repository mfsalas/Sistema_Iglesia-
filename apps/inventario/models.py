from django.db import models

from apps.ministerio.models import Ministerios


class Unidadad_de_Medida(models.Model):
    nombre_unidad = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_unidad

class Articulo(models.Model):
    descripcion_articulo = models.CharField(max_length=50)
    cantidad_articulo = models.PositiveSmallIntegerField()
    id_unidad_de_medida = models.ForeignKey(Unidadad_de_Medida, null=True, blank=True, on_delete=models.CASCADE)
    id_ministerio = models.ForeignKey(Ministerios, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion_articulo
