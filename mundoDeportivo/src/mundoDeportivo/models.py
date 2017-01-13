from __future__ import unicode_literals
from django.utils.encoding import force_bytes
from django.db import models

# Create your models here.

#===============================================================================
# class Registrado(models.Model):
#     email = models.EmailField()
#     password= models.CharField(max_length=90)
#     timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
#     
#     def __unicode__(self):
#         return self.email
# 
#     def __str__(self):
#         return self.email
#===============================================================================
    
    

class Equipo(models.Model):
    nombreEquipo = models.CharField(max_length=80)
    
    def __str__(self):
        return force_bytes(self.nombreEquipo)
    
    def __unicode__(self):
        return self.nombreEquipo
    
    def get_absolute_url(self):
        view_name = 'equipos'
        return reverse(view_name, kwars={'pk':self.nombreEquipo})
    
    
    
class Noticia (models.Model):
    idNoticia = models.AutoField(primary_key=True)
    nombreEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    tituloNoticia = models.CharField(max_length=600)
    enlace = models.URLField()
    fecha = models.DateField(auto_now=False,auto_now_add=False)
    noticia = models.TextField(max_length=9000)
    
    def __str__(self):
        return force_bytes(self.tituloNoticia)
    
    
    def __unicode__(self):
        return self.tituloNoticia
    
    def get_absolute_url(self):
        view_name = 'noticias'
        return reverse(view_name, kwars={'pk':self.idNoticia})