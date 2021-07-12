import os
from django.contrib.gis.utils import LayerMapping
from .models import warehouse

# To load the data to the db
# We need to enter the  shell to load the layers

#python manage.py shell
#>> from geo import load_layer
#>> load_layer.run()

warehouse_mapping = {
    'objectid': 'OBJECTID',
    'adm2_tr': 'adm2_tr',
    'adm2_en': 'adm2_en',
    'adm1_tr': 'adm1_tr',
    'adm1_en': 'adm1_en',
    'adm1': 'adm1',
    'pcode': 'pcode',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'POINT',
}

warehouse_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/rnd_wh.shp'))

def run(verbose=True):
    lm = LayerMapping(warehouse, warehouse_shp, warehouse_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)