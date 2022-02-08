#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACd20759027fccffb4118d24042ef21f99"
# Your Auth Token from twilio.com/console
auth_token  = "9933c63fbe721eb0b8c033b2fa026644"
client = Client(account_sid, auth_token)

lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']

#A variável mes poderia ter qualquer outro nome e ainda 

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'C:/Users/paola.miranda/Documents/Python/Hashtag/{mes}.xlsx')
    
#Esse any no final da linha serve pra verificar se algum valor na coluna é maior que 55000    
#Porque eu não quero a coluna inteira, só vendas nesse valor específico
    if (tabela_vendas['Vendas'] > 55000).any():
#Quando loc dá uma resposta, ele faz uma espécie de tabela, por isso se usa o .values[0]        
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes}, alguém bateu a meta! Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5551933003097", 
            from_="+19033213071",
            body= f'No mês de {mes}, alguém bateu a meta! Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)







# In[ ]:





# In[ ]:




