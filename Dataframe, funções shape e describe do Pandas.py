#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
alunosDic = {"Nome":["Ricardo", "Pedro", "Roberto", "Carlos"],
            "Nota":[4,7,5.5,9],"Faltas":[1,0,2,1], "Aprovado":["Não", "Sim", "Não", "Sim"]}
alunosDF = pd.DataFrame(alunosDic)


# In[19]:


print(alunosDF)
#.head formata com um
cabeçalho
alunosDF.head()


# In[20]:


#.shape informa o número de linhas e colunas do dataframe
alunosDF.shape


# In[24]:


#Fução que traz informações sobre os dados numéricos
alunosDF.describe()


# In[ ]:




