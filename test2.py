from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("C:/Users/ywu156243/Documents/Yong Wu/rawDATA/SPC919/plot.csv",sep=',',  engine = "python")
#define grid
xi = np.linspace(min(df.X), max(df.X), 100)
yi = np.linspace(min(df.Y), max(df.Y), 100)
x = df.X
y = df.Y
z = df.T1
# grid the data
zi = griddata(x, y, z, xi, yi, interp = 'linear')
#Contour the data
CS = plt.contour(xi, yi, zi, 15, linewidths = 0.5, colors = 'k')
CS = plt.contourf(xi, yi, zi, 15, cmap='rainbow')
plt.colorbar()
#plot data points
plt.scatter(x,y, marker = 'o', c='b', s=5, zorder =10)
plt.xlim(min(x),max(x))
plt.ylim(min(y),max(y))
plt.show()