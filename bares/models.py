# -*- coding: utf-8 -*-

from django.db import models
#from django.template.defaultfilters import slugify

class Bares(models.Model):
    id_bar = models.AutoField(primary_key=True)
    nombre_bar = models.CharField(max_length=30, unique=True)
    direccion = models.CharField(max_length=128)
    visitas = models.IntegerField(default=0)
    #slug = models.SlugField(unique=True)

#   def save(self, *args, **kwargs):
#       self.slug = slugfy(self.nombre_bar)
#       super(Bares, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre_bar

class Tapas(models.Model):
    id_tapa = models.AutoField(primary_key=True)
    nombre_tapa = models.CharField(max_length=30)
    votos = models.IntegerField(default=0)
    bar = models.ForeignKey(Bares)

    def __unicode__(self):
        return self.nombre_tapa
