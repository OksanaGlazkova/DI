#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import datetime, timedelta


# In[2]:


data = {'customer_id':[1, 1, 1, 1, 2, 2, 2, 2, 2], 'product_id':[10, 11, 12, 13, 14, 15, 16, 17, 18], 'timestamp':['2008-11-18 17:20:19', '2008-11-18 17:21:20', '2008-11-18 17:30:30', '2008-11-18 17:21:21', '2008-11-18 17:25:25', '2008-11-18 17:31:31', '2008-11-18 17:31:31', '2008-11-18 17:38:38', '2008-11-18 17:39:39']}


# In[3]:


df = pd.DataFrame(data)
df


# In[4]:


df['id'] = list(range(len(df.sort_values(['customer_id', 'timestamp']))))
df['id'] = df['id']+1


# In[5]:


df['timestamp'] = pd.to_datetime(df['timestamp'])


# In[7]:


session = df.sort_values(['customer_id', 'timestamp'])[['id', 'customer_id','timestamp']]
session


# In[8]:


session['diffs'] = session.groupby('customer_id')['timestamp'].diff().dt.seconds
session


# In[9]:


sessions_start = session[(session['diffs'].isnull()) | (session['diffs'] > 180)]
sessions_start['session_id'] = sessions_start['id']
sessions_start


# In[10]:


df = df.sort_values('id')
sessions_start = sessions_start.sort_values('id')
df = pd.merge_asof(df, sessions_start[['id','customer_id', 'session_id']], on='id' ,by='customer_id')
df


# In[11]:


df = df[['customer_id', 'product_id', 'timestamp', 'session_id']]
df


# In[ ]:




