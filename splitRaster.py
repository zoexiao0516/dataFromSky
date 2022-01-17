#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 00:53:18 2021

@author: zoeyajiexiao
"""


from osgeo import gdal

data = gdal.Open("Data/F182013.v4c_web.avg_vis.tif")
gt = data.GetGeoTransform()

# get coordinates of upper left corner
xmin = gt[0]
ymax = gt[3]
res = gt[1]

# determine total length of raster
xlen = res * data.RasterXSize
ylen = res * data.RasterYSize

# number of tiles in x and y direction
xdiv = 43201
ydiv = 16801

# size of a single tile
xsize = xlen/xdiv
ysize = ylen/ydiv

# create lists of x and y coordinates
xsteps = [xmin + xsize * i for i in range(xdiv+1)]
ysteps = [ymax - ysize * i for i in range(ydiv+1)]

# loop over min and max x and y coordinates
for i in range(xdiv):
    for j in range(ydiv):
        xmin = xsteps[i]
        xmax = xsteps[i+1]
        ymax = ysteps[j]
        ymin = ysteps[j+1]
        
        # print("xmin: "+str(xmin))
        # print("xmax: "+str(xmax))
        # print("ymin: "+str(ymin))
        # print("ymax: "+str(ymax))
        # print("\n")
        
        # use gdal warp
        gdal.Warp("tile"+str(i)+str(j)+".tif", data, 
                  outputBounds = (xmin, ymin, xmax, ymax), dstNodata = -9999)
        # or gdal translate to subset the input raster
        # gdal.Translate("data_translate"+str(i)+str(j)+".tif", data, projWin = (xmin, ymax, xmax, ymin), xRes = res, yRes = -res)
        
# close the open dataset!!!
data = None
        
        