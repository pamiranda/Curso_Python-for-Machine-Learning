#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Isso é um dicionário
import pandas as pd
alunos = {"Nome":['Ricardo', 'Pedro', 'Roberto', 'Carlos'], 
          'Nota':[4,7,5.5,9],
           'Aprovado':['Não', 'Sim', 'Não','Sim']  }
df =pd.DataFrame(alunos)


# In[6]:


print(df)


# In[7]:


#Series cria vetores unidirecionais
#"series é como um dataframe de uma coluna só"
objeto1 = pd.Series([2,6,9,10,5])
print(objeto1)


# In[10]:


import numpy as np
array = pd.array([2,6,9,10,5])
print(array)


# In[ ]:




