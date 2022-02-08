#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
dados = pd.read_csv('C:/Users/paola.miranda/Documents/didaticatech/athelet.csv')
dados.head()
# nan significa dados não informados, ou zero


# In[31]:


#Com o comando inplace é feita a alteração sem imprimir o resultado

dados.rename(columns = {'Ability': "Habilidade",'Hours_Spent_On_Homework_Per_Week':'Horas', "School": "Escola"}, inplace = True)


# In[ ]:


categoria = dados['Escola']


# In[ ]:


type(categoria)


# In[33]:


#.value_counts() conta todos os valores
dados['Horas'].value_counts()


# In[ ]:




