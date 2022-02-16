#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
dados = pd.read_excel(r'C:\Users\paola.miranda\Documents\Python\didaticatech\despesa.xlsx')
dados.head(100)


# In[9]:


import matplotlib.pyplot as plt
dados.boxplot(column ='Valor Real')
plt.show()


# In[ ]:




