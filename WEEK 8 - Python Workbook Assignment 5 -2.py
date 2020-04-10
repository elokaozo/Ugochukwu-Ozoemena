#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]


# In[2]:


GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data=GradeList,
 columns=['Names','Grades','bsdegrees','msdegrees','phddegrees'])
df


# In[3]:


df['Grades'].count() 


# In[4]:


df['bsdegrees'].mean() 


# In[5]:


df['msdegrees'].std() 


# In[6]:


df['phddegrees'].min() 


# In[7]:


df['Grades'].max() 


# In[8]:


df['Grades'].quantile(.25)


# In[9]:


df['Grades'].quantile(.5) 


# In[10]:


df['Grades'].quantile(.75)


# In[11]:


df['msdegrees'].median()


# In[12]:


df['msdegrees'].mode()


# In[13]:


df.var()


# In[ ]:




