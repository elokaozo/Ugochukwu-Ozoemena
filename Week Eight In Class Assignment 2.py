#!/usr/bin/env python
# coding: utf-8

# In[5]:



import pandas as pd
import numpy as np
import folium
import matplotlib.pyplot as plt
data=pd.read_csv('covid file 03-30-20.csv')
data


# In[18]:


import plotly.graph_objects as go

 

fig = go.Figure(data=go.Scattergeo(
        lon = data['Long_'],
        lat = data['Lat'],
        mode = 'markers',
        ))

 

fig.update_layout(
        title = 'Corona Virus Cases in the US)',
        geo_scope='world',
    )
fig.show()


# In[ ]:





# In[ ]:




