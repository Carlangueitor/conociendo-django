from django.db import models
from django.conf import settings


class Tweet(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    texto = models.TextField()
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    
