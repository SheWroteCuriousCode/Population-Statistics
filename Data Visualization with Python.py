#!/usr/bin/env python
# coding: utf-8

# In[22]:


data= pd.read_csv ('countries.csv')


# In[23]:


data


# In[25]:


data.country== 'United States'


# In[26]:


US= data[data.country == 'United States']


# In[27]:


US


# In[28]:


China= data[data.country == 'China']


# In[29]:


China


# In[33]:


plt.plot (US.year, US.population / 10**6)
plt.plot (China.year, China.population/ 10**6)
plt.xlabel ("Year")
plt.ylabel ("Population")
plt.legend (["United States", "China"])
plt.show ()


# In[ ]:




