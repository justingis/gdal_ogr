#-------------------------------------------------------------------------------
# Name:        gis_input.py
# Description: Gets input GIS data and creates layers that can be passed to the gis_analysis.py module
#
# Author:      Justin Hawley (justin.hawley777@gmail.com)
#
# Created:     03/12/2023
#
# Interpreter: /gdal_ogr/venv/bin/python3
#-------------------------------------------------------------------------------

import sys
from osgeo import ogr
import os

def get_layer(path, layer_name = None, read_only = 0):
    file_name, file_extension = os.path.splitext(path)
    if file_extension == '.shp':
        fn = path
        ds = ogr.Open(fn, read_only)
        if ds is None:
            sys.exit('Could not open {0}.'.format(fn))
        else:
            lyr = ds.GetLayer(0)
            return [lyr, ds]

    elif file_extension == '.gdb':
        ogr.UseExceptions()
        driver = ogr.GetDriverByName("OpenFileGDB")
        try:
            gdb = driver.Open(path, 0)
        except Exception as e:
            print (e)
            sys.exit()
        for featsClass_idx in range(gdb.GetLayerCount()):
            lyr = gdb.GetLayerByIndex(featsClass_idx)
            if lyr.GetName() == layer_name:
                return [lyr, gdb]
    else:
        sys.exit('Invalid file type...')


def main():
      #my_layer = get_layer(r'/Users/justinhawley/Desktop/my_gdb.gdb','centroids')
      #print(my_layer)
      pass

if __name__ == '__main__':
    main()
