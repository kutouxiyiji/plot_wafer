from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("C:/Users/ywu156243/Documents/Yong Wu/rawDATA/SPC919/plot.csv",sep=',',  engine = "python")
#define grid
xi = np.linspace(min(df.X) - 3, max(df.X) + 3, 100)
yi = np.linspace(min(df.Y) - 3, max(df.Y) + 3, 100)
x = df.X
y = df.Y
z = df.T1
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
plt.savefig("C:/Users/ywu156243/Documents/Yong Wu/rawDATA/SPC919/S1.png", dpi = 300,  transparent = True, aspect = 2)

plt.show()