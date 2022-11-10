#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlite3 as sl


# In[2]:


con = sl.connect('my-test.db')


# In[7]:


with con:
    con.execute("""
        create table product (
	      id serial primary key,
	      product_name varchar(100) not null
	      );
    """)


# In[9]:


sql = 'INSERT INTO product (id, product_name) values(?, ?)'
data_product = [
    ('1', 'baby milk'),
    ('2', 'cucumber'),
    ('3', 'cheese'),
    ('4', 'strawberry')    
]


# In[10]:


with con:
    con.executemany(sql, data_product)


# In[11]:


with con:
    con.execute("""
        create table category (
	      id serial primary key,
	      category_name varchar(100) not null
      	);
    """)


# In[12]:


sql = 'INSERT INTO category (id, category_name) values(?, ?)'
data_category = [
    ('1', 'milky'),
    ('2', 'vegetables'),
    ('3', 'meat'),
    ('4', 'baby')
]


# In[13]:


with con:
    con.executemany(sql, data_category)


# In[14]:


with con:
    con.execute("""
        create table category_product (
	      id serial primary key,
	      id_product integer references product(id),
	      id_category integer references category(id)
	      );
    """)


# In[15]:


sql = 'INSERT INTO category_product (id, id_product, id_category) values(?, ?, ?)'
data_category_product = [
    ('1', '1', '1'),
    ('2', '1', '4'),
    ('3', '2', '2'),
    ('4', '3', '1')
]


# In[16]:


with con:
    con.executemany(sql, data_category_product)


# In[17]:


sql = 'INSERT INTO category_product (id, id_product) values(?, ?)'
data_category_product = [
    ('5', '4')
]


# In[18]:


with con:
    con.executemany(sql, data_category_product)


# In[19]:


sql = 'INSERT INTO category_product (id, id_category) values(?, ?)'
data_category_product = [
    ('6', '3')
]


# In[20]:


with con:
    con.executemany(sql, data_category_product)


# In[21]:


df_product = pd.read_sql('''SELECT * FROM product''', con)
df_product


# In[22]:


df_category = pd.read_sql('''SELECT * FROM category''', con)
df_category


# In[23]:


df_category_product = pd.read_sql('''SELECT * FROM category_product ''', con)
df_category_product


# In[24]:


df1 = pd.read_sql('''select distinct product_name, category_name
from product p
left join category_product cp on p.id = cp.id_product
left join category c on cp.id_category = c.id''', con)
df1


# In[25]:


df2 = pd.read_sql('''select distinct category_name, product_name
from category c
left join category_product cp on c.id = cp.id_category
left join product p on cp.id_product = p.id''', con)
df2


# In[26]:


df3 = pd.read_sql('''select distinct product_name, category_name
from product p
left join category_product cp on p.id = cp.id_product
left join category c on cp.id_category = c.id
Union
select distinct product_name, category_name
from category c
left join category_product cp on c.id = cp.id_category
left join product p on cp.id_product = p.id''', con)
df3


# In[ ]:




