#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
dados = pd.read_csv(r'C:\Users\paola.miranda\Documents\Python\didaticatech\athelet.csv')
dados.head()


# In[6]:


import matplotlib.pyplot as plt


# In[10]:


dados.hist(column="Hours_Spent_On_Homework_Per_Week", bins = 10 )
plt.show()


# In[ ]:




