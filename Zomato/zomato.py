#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 14:35:21 2018

@author: jai
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import mlab

df=pd.read_csv('zomato.csv', encoding='latin-1')
df.describe()
df.head(5)

lat = delhi['Latitude'].values
lon = delhi['Longitude'].values
cost = delhi['Average Cost for two'].values
rating = delhi['Aggregate rating']
geo=(lat, lon)

indian=df.loc[df['Currency']=='Indian Rupees(Rs.)']

delhi=indian.loc[df['City']=='New Delhi']


fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution='c', 
            lat_0=22.7961882, lon_0=76.4576492,
            width=20, height=20)

map = Basemap(projection='cyl', lat_0=22.7961882, lon_0=76.4576492)
map.drawmapboundary(fill_color='#4CC4FF')
map.drawcountries(color='black')
map.drawstates(color='black')
map.drawcoastlines()
#map.fillcontinents(color='#4cb47d',lake_color='aqua')
map.scatter(lon, lat, latlon=True, marker='D', color='red')


plt.scatter(rating, delhi['Votes']) 

plt.scatter(lat, lon, c=rating, s=25, edgecolors='')
plt.colorbar()


plt.scatter(lat, lon, c=cost, s=25, edgecolors='', alpha=0.25)
plt.colorbar()

plt.bar(rating, cost)    

