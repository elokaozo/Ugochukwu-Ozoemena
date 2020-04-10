#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


plt.scatter(df['hours'], df['grade'])

plt.xlabel("Hours")

plt.ylabel("Grades")

plt.title("Scatter plot of student grades and hours")


# In[ ]:


#Yes, Grades are increasing as hours are increasing

