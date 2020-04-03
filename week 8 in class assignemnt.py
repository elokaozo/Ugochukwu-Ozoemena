#!/usr/bin/env python
# coding: utf-8

# In[5]:



import pandas as pd
import numpy as np
import folium
import matplotlib.pyplot as plt
data=pd.read_csv('covid file 03-30-20.csv')
data


# In[12]:


m = folium.Map(location=[0, 0], tiles="Stamen Toner", zoom_start=2)

data = pd.read_csv('covid file 03-30-20.csv')

# I can add marker one by one on the map

for i in range(0,len(data)):

   pd.read_csv('covid file 03-30-20.csv')

   folium.Circle(

      location=[data.iloc[i]['Lat'], data.iloc[i]['Long_']],

      popup=data.iloc[i]['Country_Region'],

     radius=float(*5),
      color='red',

      fill=True

   ).add_to(m)

m


# In[ ]:




