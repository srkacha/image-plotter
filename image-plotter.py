import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
image = imread('jake.jpg')

imageHeight = len(image)
imageWidth = len(image[0])

plt.figure()

for yindex, y in enumerate(image):
    for xindex, rgb in enumerate(y):
        r = rgb[0]/255
        g = rgb[1]/255
        b = rgb[2]/255
        color = tuple((r, g, b))
        xPlot = xindex + 1
        yPlot = imageHeight - yindex
        plt.plot(xPlot, yPlot, marker = '.', color = color, markersize = 3)
        

plt.show()   