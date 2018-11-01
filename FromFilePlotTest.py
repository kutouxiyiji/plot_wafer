# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 00:24:58 2017

@author: YWu156243
"""

from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def ContourPlot(x,y,z,slot,path):
    xi = np.linspace(min(x) - 3, max(x) + 3, 100)
    yi = np.linspace(min(y) - 3, max(y) + 3, 100)
    # grid the data
    zi = griddata(x, y, z, xi, yi, interp = 'linear')
    #Contour the data
    CS = plt.contour(xi, yi, zi, 15, linewidths = 0.5, colors = 'k')
    CS = plt.contourf(xi, yi, zi, 15, cmap='rainbow')
    plt.colorbar(orientation = 'vertical')
    #plot data points
    plt.scatter(x,y, marker = 'o', c='b', s=10, zorder =10)
    plt.xlim(min(x) - 3,max(x) + 3)
    plt.ylim(min(y) - 3,max(y) + 3)
    for i, thk in enumerate(z):
        CS = plt.annotate(format(thk, '.2f'), (x[i], y[i]), fontsize = 8) #2 digits after the point
        #plt.figure(figsize = (10,10))
    plt.savefig(path + "figure/S{}.png".format(slot), dpi = 300,  transparent = True, aspect = 2)
    plt.show()
    
df = pd.read_csv("C:/Users/ywu156243/Documents/Yong Wu/rawDATA/SPC919/testMOD.csv",sep=',',  engine = "python")
slot = 1
j=0
path = "C:/Users/ywu156243/Documents/Yong Wu/rawDATA/SPC919/"
for i in range(len(df)):
    if df.T1[i] != 'T1':
        x[j] = df.X[i]
        y[j] = df.Y[i]
        z[j] = df.T1[i]
        j +=1
    else:
        ContourPlot(x,y,z,slot,path)
        slot +=1
        j=0
ContourPlot(x,y,z,slot,path)