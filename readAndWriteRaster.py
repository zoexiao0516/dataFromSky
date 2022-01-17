# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
try:
    from osgeo import gdal
except ImportError:
    import gdal
    
import numpy as np
import matplotlib.pyplot as plt

# import 
ds = gdal.Open("Data/roughness_NY.tif")

# from image coordinate to geographic coordinates
gt = ds.GetGeoTransform()  
# https://gdal.org/tutorials/geotransforms_tut.html

proj = ds.GetProjection()

band = ds.GetRasterBand(1)  # this data has only one band
array = band.ReadAsArray()

plt.figure()
plt.imshow(array)

# manipulate
# element that is greater than the mean will be assigned to 1
binmask = np.where((array >= np.mean(array)),1,0)  
# plt.figure()
# plt.imshow(binmask)
idn = np.identity(array.shape[0])
idnMinusA = idn - array
idnMinusAInv = np.linalg.inv(idnMinusA) 

# export
driver = gdal.GetDriverByName("GTiff")
driver.Register()
outds = driver.Create("roughness_idnMinusAInv_NY.tif", xsize = idnMinusAInv.shape[1],
                      ysize = idnMinusAInv.shape[0], bands = 1, 
                      eType = gdal.GDT_Int16)
outds.SetGeoTransform(gt)
outds.SetProjection(proj)
outband = outds.GetRasterBand(1)
outband.WriteArray(binmask)
outband.SetNoDataValue(np.nan)
outband.FlushCache()

# close your datasets and bands
outband = None
outds = None
