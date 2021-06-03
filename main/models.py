from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.db import models as gis_models


# Create your models here.
class Country(models.Model):
    tittle = models.CharField('Название', max_length=50, primary_key=True)  # primary_key=True
    location = models.MultiPolygonField(srid=4326)
    # objects = gis_models.Manager()

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Town(models.Model):
    tittle = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=50)
    photos = models.CharField('Фотографии', max_length=50)
    location = gis_models.MultiPolygonField(srid=4326)
    objects = gis_models.Manager()
    country = models.ForeignKey('Country', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Capital(models.Model):
    tittle = models.CharField('Название', max_length=50)
    location = gis_models.MultiPolygonField(srid=4326)
    objects = gis_models.Manager()
    country = models.OneToOneField(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = 'Столица'
        verbose_name_plural = 'Столицы'
