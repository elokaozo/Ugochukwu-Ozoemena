#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[5]:


df['genderint'] = np.where(df['gender']=='female',1, 0 )
df.head()



# In[6]:


import statsmodels.formula.api as sm 

result = sm.ols(formula='grade ~ genderint + exercise + hours',data=df).fit()

result.summary()



# In[7]:


#genderint Does not improve R-squared


# In[ ]:




