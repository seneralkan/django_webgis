import os
from django.contrib.gis.utils import LayerMapping
from .models import counties

# To load the data to the db
# We need to enter the  shell to load the layers

#python manage.py shell
#>> from geo import load_layer
#>> load_layer.run()


counties_mapping = {
    'adm1_tr': 'adm1_tr',
    'adm1_en': 'adm1_en',
    'adm1': 'adm1',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'adm0_en': 'adm0_en',
    'adm0_tr': 'adm0_tr',
    'adm0': 'adm0',
    'geom': 'MULTIPOLYGON',
}


county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/tur_polbnda_adm1.shp'))

def run(verbose=True):
    lm = LayerMapping(counties, county_shp, counties_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)