from django.db import models

# Create your models here.
class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion=models.TextField()
    tecnologias = models.CharField(max_length=200)
    link= models.CharField(max_length=150)
    imagen = models.FilePathField(path='/img')



# p1=Proyecto(titulo='SGI de Pozos Petroleros', \
# descripcion='Plataforma web para la gestion de datos de pozos \
# petroleros de estacion Caimancito', tecnologias='SQL Server, ASP, \
# Codecharge', link='https://www.lanacion.com', imagen='static/img/pozos.png')
# p1.save()
# from portfolio.models import Proyecto

# p4=Proyecto(titulo="SGI Toners y Reciclados", \
# descripcion="Aplicacion de escritorio para la gestion de reciclados de \
# toner de ECIN", tecnologias="VB SQL", \
# link="https://www.ecinsoluciones.com", imagen="img/ecin.png")
# p4.save()

