#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
alunosDic = {"Nome":["Paola", "Ian","André", "Anna"], "Nota":[7,8,7,9.], "Aprovado":['Sim', 'Sim', 'Não', 'Sim']}
alunosDF = pd.DataFrame(alunosDic)
print(alunosDF)
alunosDF.head()


# In[7]:


#Estou jogando todos os dados que satisfazem essa condição dentro de uma variável nova
primeiraslinhas = alunosDF.loc[0:1]


# In[8]:


print(primeiraslinhas)


# In[14]:


novoDF = alunosDF.loc[alunosDF["Nota"]!=9]
print(novoDF)


# In[16]:


alunosAprovados = alunosDF.loc[alunosDF["Aprovado"]=='Não']
print(alunosAprovados)


# In[ ]:




