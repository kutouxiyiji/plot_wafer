# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:52:06 2017

@author: KTXYJ
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from bokeh.plotting import figure, show, output_file

sns.set(color_codes=True)
df = pd.read_csv("C:/Users/ywu156243/Documents/Yong Wu/rawDATA/SPC919/plot.csv",sep=',',  engine = "python")

df2 = df.pivot('X','Y','T1') #save to a matrix dataframe df2

#sns.jointplot(x="X", y="Y", data=df['T1'], kind="kde");
#sns.kdeplot(df['X'], df['Y'], n_levels=10, shade=True)

#ax = sns.heatmap(df2, robust = True, cmap="RdYlGn")
#fig = plt.figure()
#ax = Axes3D(fig)
#df.plot_trisurf(df['X'], df['Y'], df['T1'], cmap=cm.jet, linewidth=0.2)
#plt.show()
#df.plot.scatter(x='X', y='Y', s =df['T1']*20, color='DarkBlue', label='Group 1')
f, ax = plt.subplots(figsize=(7,5))
sns.heatmap(df2, annot=True, fmt="d", linewidths=.1, ax=ax)
