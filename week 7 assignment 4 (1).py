#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()
bins = [0,80,100]
group_names = ['Fail', 'Pass']
df['Pass/Fail'] = pd.cut(df['grade'], bins, labels=group_names)
df


# In[ ]:




