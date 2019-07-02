#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df_o= pd.read_csv('../db/votacao_proposicao_orientacao.csv')
df_v= pd.read_csv('../db/votacao_proposicao.csv')


# In[3]:


df_vp=df_v.copy()
# df_vp.head(2)


# In[4]:


df_op=df_o.copy()
# df_op.head(2)


# In[5]:


df_op_dp = pd.DataFrame()
df_vp_dp = pd.DataFrame()

df_op_dp['prop'] = df_op['id_proposicao']
df_vp_dp['prop'] = df_vp['id_proposicao']

df_op_dp['data_hora_o'] = pd.to_datetime(df_op['data_votacao'] + ' ' + df_op['hora_votacao'])
df_vp_dp['data_hora_v'] = pd.to_datetime(df_vp['data_votacao'] + ' ' + df_vp['hora_votacao'])


# df_op_dp.head()


# In[6]:


# df_op['prop_data_hora_o'] = df_op['id_proposicao'] + df_op['space'] +df_op['data_hora_o']
# df_vp['prop_data_hora_v'] = df_vp['id_proposicao'] + df_vp['space'] +df_vp['data_hora_v']
# df_op['prop'] = df_op['prop'].astype(str)
# df_op['data_hora_o'] = df_op['data_hora_o'].astype(str)
# df_op['prop_data_hora_o'] = df[['prop','data_hora_o']].apply(' '.join, axis=1)

df_op['prop_data_hora_o'] = df_op_dp.apply(lambda x: ' '.join(x.astype(str)), axis=1)
df_vp['prop_data_hora_o'] = df_vp_dp.apply(lambda x: ' '.join(x.astype(str)), axis=1)


# In[7]:


df_vp.head(2)


# In[8]:


df_op.to_csv('../db/votacao_proposicao_orientacao_prop_data_hora.csv', encoding='utf-8', index=False)
df_vp.to_csv('../db/votacao_proposicao_prop_data_hora.csv', encoding='utf-8', index=False)


# In[ ]:




