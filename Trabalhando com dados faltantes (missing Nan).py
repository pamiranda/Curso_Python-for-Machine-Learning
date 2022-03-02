#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
dados = pd.read_excel(r"C:\Users\paola.miranda\Documents\Dev\Python\didaticatech\testeexcel2.xlsx")


# In[31]:


dados.head(20)


# In[20]:


dados2 = dados.dropna()


# In[25]:


dados2.shape


# In[24]:


enulo = dados.isnull().sum()
enulo.head()


# In[27]:


faltantesPercentual = dados.isnull().sum() / len(dados["Valor Estimado"])*100


# In[28]:


faltantesPercentual.head()


# In[35]:


dados['Valor Estimado'].fillna("Nenhuma", inplace = True)
dados['Valor Real'].fillna('Valor Real').mean()


# In[ ]:




