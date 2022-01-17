# Python Manipulation of Raster Data

readAndWriteRaster.py: read the raster data and get the transformed roughness matrix data: the inverse of (identity matrix - matrix)
splitRaster.py: split the data by specifying the number of tiles in x and y direction
calcCorr.py: vectorize the matrix and calculate the correlation coefficient between light data matrix and transformed roughness data matrix (right now I can only do one pair at a time)
