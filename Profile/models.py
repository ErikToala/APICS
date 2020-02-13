from django.db import models
from django.utils import timezone


class Genero(models.Model):         #1
    sexo = models.CharField(max_length=250, null= False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sexo

    class Meta:
        db_table='Genero'


class Estado_civil(models.Model):               #2
    estado_civil = models.CharField(max_length=250, null= False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.estado_civil

    class Meta:
        db_table='EstadoCivil'

  
class Ocupacion(models.Model):                   #3
    ocupacion = models.CharField(max_length=250, null= False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ocupacion

    class Meta:
        db_table='Ocupacion'


class Estado(models.Model):                        #4
    nombre = models.CharField(max_length=250, null= False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table='Estado'


class Ciudad(models.Model):                            #5
    ciudad = models.CharField(max_length=250, null= False)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ciudad

    class Meta:
        db_table='Ciudad'


class Profile2(models.Model):                           #6
    nombre = models.CharField(max_length=250, null= False)
    apePaterno = models.CharField(max_length=250, null= False)
    apeMaterno = models.CharField(max_length=250, null= False)
    edad = models.IntegerField(null=False)
    ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    ocupacion = models.ForeignKey(Ocupacion,on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    estado_civil = models.ForeignKey(Estado_civil,on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table='Profile'

# Create your models here.