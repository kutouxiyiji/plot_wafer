# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
user: KTXYJ
Clean Data
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import math
import numpy as np

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


#read csv, skip first 29rows until real data
df = pd.read_csv("C:/Users/ywu156243/Documents/Yong Wu/rawDATA/SPC919/test_new.csv",skiprows=29, sep=',',  engine = "python")
#only select 'X', 'Y'.... columns
df = df[['X','Y','T1']]
#edit data, FLAG none-data rows
#times the XRF counts coficients
for i in range(len(df)):
    if isNaN(df['X'][i]) or df['X'][i] == None:
        df['T1'][i] = 'FLAG'
    elif is_number(df['T1'][i]):
        df['T1'][i] = 2*float(df['T1'][i].encode('utf-8')) # problem cant add str + int, and cant use int() because data has overflow problem

#delete FLAG rows
df = df[df.T1 != 'FLAG']

#save to csv 
df.to_csv('C:/Users/ywu156243/Documents/Yong Wu/rawDATA/SPC919/testMOD.csv')