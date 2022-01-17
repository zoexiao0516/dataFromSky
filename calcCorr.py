#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 02:01:13 2021

@author: zoeyajiexiao
"""

try:
    from osgeo import gdal
except ImportError:
    import gdal
    
import numpy as np
import matplotlib.pyplot as plt

# import 
ds1 = gdal.Open("Data/roughness_split/roughness_split.5984.tif")
ds2 = gdal.Open("Data/light_split/light_split.5984.tif")

# from image coordinate to geographic coordinates
gt1 = ds1.GetGeoTransform()  
gt2 = ds2.GetGeoTransform()  
# https://gdal.org/tutorials/geotransforms_tut.html

proj1 = ds1.GetProjection()
proj2 = ds2.GetProjection()

band1 = ds1.GetRasterBand(1)  # this data has only one band
band2 = ds2.GetRasterBand(1)
array1 = band1.ReadAsArray()
array2 = band2.ReadAsArray()

idn1 = np.identity(array1.shape[0])
idn1MinusA = idn1 - array1
idn1MinusAInv = np.linalg.inv(idn1MinusA) 

plt.figure()
plt.imshow(array1)

# vectorize
vector_array1 = idn1MinusAInv.flatten()
vector_array2 = array2.flatten()

# calculate correlation between 2 vectors   
print(np.corrcoef(vector_array1,vector_array2))
