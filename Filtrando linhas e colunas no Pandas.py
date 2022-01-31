#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
alunosDic = {"Nome":["Paola", "Ian","André", "Anna"], "Nota":[7,8,7,5.], "Aprovado":['Sim', 'Sim', 'Não', 'Sim']}
alunosDF = pd.DataFrame(alunosDic)
print(alunosDF)
alunosDF.head()


# In[17]:


#Esse comando filtra o dataframa por colunas, exibindo todas as informações sobre ela, fatiamento de daframe, "slice"
alunosDF ['Nota']


# In[6]:


#Esse filtra as linhas através dos indices
alunosDF.loc[0:2:2]


# In[15]:


#Filtro
alunosDF.loc[alunosDF["Aprovado"]=="Não"]


# In[ ]:




