#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('C:\\Users\\santa\\OneDrive\\Documents\\reports.csv')


# In[3]:


df


# In[4]:


df['Physics'].median()


# In[5]:


df = pd.read_csv('C:\\Users\\santa\\OneDrive\\Documents\\reports.csv',index_col = 'Date_of_birth', parse_dates=True)


# In[6]:


df


# In[7]:


df.sort_values('Date_of_birth')


# In[8]:


import numpy as np


# In[9]:


df.drop_duplicates()


# In[10]:


df.set_index(['Name','City']).count(level = 'City').sort_values('City')


# In[11]:


df.groupby('City')['Maths'].mean()


# In[12]:


df.groupby('City')[['Maths','Physics']].median()


# In[13]:


df.groupby(['City','Place'])[['Maths','Physics']].mean()


# In[14]:


df.pivot_table(index="Place",values='Chemistry')


# In[15]:


df.pivot_table(index="Place",values='Chemistry',aggfunc=[np.median])


# In[16]:


df.pivot_table(index="Place",values='Chemistry',aggfunc=[np.mean,np.median])


# In[17]:


df.pivot_table(index='Name',columns='City',values='Maths')


# In[18]:


df.reset_index()


# In[20]:


df['Maths'].quantile(0.5)


# In[22]:


df[['Maths','Physics']].quantile(0.5)


# In[23]:


df['Maths'].quantile([0.5,0.3])


# In[26]:


df['Maths'].cumsum()


# In[36]:


df['City'].count()


# In[40]:


df.groupby('City')[['Maths','Physics']].min()


# In[42]:


df.groupby('City')[['Maths','Physics']].max()


# In[54]:


df.groupby('City')[['Maths','Physics']].sum()


# In[44]:


df.pivot_table(index="Place",values='Chemistry',aggfunc=[np.median])


# In[60]:


exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [80, 90, 35, 70, 93, 70, 45, 40, 88, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'no', 'yes', 'no']}

exam = pd.DataFrame(exam_data)
exam


# In[63]:


exam['mean'] = exam['score']/2


# In[64]:


exam


# In[65]:


df.set_index(['Name','City']).count(level = 'City').sort_values('City')


# In[66]:


df


# In[74]:


df['City'].count()


# In[81]:


df


# In[88]:


df.set_index('City')


# In[90]:


df1=df.reset_index()


# In[91]:


df1


# In[94]:


df1['Date_of_birth'].max()


# In[95]:


df


# In[96]:


df.reset_index()


# In[ ]:




