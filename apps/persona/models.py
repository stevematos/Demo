from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.URLField()
    description = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)

class Persona(models.Model):
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    sexo = models.CharField(max_length=20)
    fecha_nac = models.DateField()
    correo_electronico = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)