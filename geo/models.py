from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
# Create your models here.

class Incidences(models.Model):
    name = models.CharField(max_length=50)
    localname = models.PointField(srid=4326)
    objects_manager = GeoManager()

    class Meta:
        db_table = 'incident'
        verbose_name_plural = 'Incidences'

    def __str__(self):
        return self.name

class counties(models.Model):
    adm1_tr = models.CharField(max_length=50)
    adm1_en = models.CharField(max_length=50)
    adm1 = models.CharField(max_length=6)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    adm0_en = models.CharField(max_length=50)
    adm0_tr = models.CharField(max_length=50)
    adm0 = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.adm1_en