# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 00:47:41 2017

@author: KTXYJ

Alpha version

Application: 1. Read and clean SPC919 data and plot all wafers' contour map
"""

from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def ContourPlot(x,y,z,slot,path):
    #draw the grid
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
    plt.savefig(path + "figure/S{}.png".format(slot), dpi = 300,  transparent = True, aspect = 2)
    plt.show()
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def isnot_number(s):
    try:
        float(s)
        return False
    except ValueError:
        return True    
    
def isNaN(num):
    return num != num

def CleanCSV(path,filename):
    #delete first 29rows to make data easier to clean. 
    df = pd.read_csv(path + filename,skiprows=29, sep=',',  engine = "python")
    #only select 'X', 'Y'.... columns
    df = df[['X','Y','T1']]
    #edit data, FLAG none-data rows
    #times the XRF counts coficients
    for i in range(len(df)):
        if isNaN(df['X'][i]) or df['X'][i] == None:
            df['T1'][i] = 'FLAG'
        elif is_number(df['T1'][i]):
            df['T1'][i] = 1*float(df['T1'][i].encode('utf-8')) # problem cant add str + int, and cant use int() because data has overflow problem
    #delete FLAG rows
    df = df[df.T1 != 'FLAG']
    #save to cleanbuffer csv 
    df.to_csv(path + "CleanBUFFER.csv")
    
    
if __name__ == '__main__':
    path = "C:/Users/ywu156243/Documents/Yong Wu/rawDATA/SPC919/"
    filename = "test_new.csv"
    CleanCSV(path,filename)
    #read cleaned data "CleanBUFFER."
    df = pd.read_csv(path + "CleanBUFFER.csv",sep=',',  engine = "python")
    #following is used to plot contour plots of all wafers in the file
    slot = 1
    j=0
    for i in range(len(df)):
        if df.X[i] != 'X':
            x[j] = df.X[i]
            y[j] = df.Y[i]
            z[j] = df.T1[i]
            j +=1
        else:
            ContourPlot(x,y,z,slot,path)
            slot +=1
            j=0
    ContourPlot(x,y,z,slot,path) #Plot last figure
