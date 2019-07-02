#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import warnings
warnings.filterwarnings('ignore')
from nltk.corpus import stopwords
import nltk

pd.options.display.max_columns = None


# In[251]:


partido = 'GOV.'


# In[252]:


df_o= pd.read_csv('../db/votacao_proposicao_orientacao_prop_data_hora.csv')
df_v= pd.read_csv('../db/votacao_proposicao_prop_data_hora.csv')


# In[253]:


df_vp=df_v.copy()
cols=['ide_cadastro','data_captura','url_captura']
df_vp = df_vp.drop(columns = cols)
# df_vp.head(2)


# In[254]:


df_op=df_o.copy()
cols=['data_captura','url_captura','numero_captura']
df_op = df_op.drop(columns = cols)
# df_op.head(2)


# In[255]:


print('Numero de partidos nas proposições Orientadas', len(list(df_op['sigla_partido'].unique())))
print('Numero de proposições Orientadas', len(list(df_op['prop_data_hora_o'].unique())))


# In[256]:


df_op = df_op[df_op['sigla_partido']==partido]
print('Proposiçoes Orientadas Pelo Partido %s'%(partido),len(list(df_op['prop_data_hora_o'] )))
# df_op.head(2)


# In[257]:


df_vp = df_vp.rename({'prop_data_hora_p':'prop_data_hora_o'})
# df_vp.head(2)


# In[ ]:





# In[258]:


check_partido = 'check_%s'%(partido)
df_op[check_partido]=1


# In[259]:


cols=['prop_data_hora_o']
df = pd.merge(df_vp , df_op, on = cols ,how = 'left')


# In[260]:


df.describe()


# In[261]:


cols = df.columns.tolist()
print(cols)


# In[262]:


cols = [ 'id_proposicao_y', 'tipo_proposicao_sigla_y', 'numero_proposicao_y', 
        'ano_proposicao_y', 'resumo_votacao_y', 'data_votacao_y', 'hora_votacao_y', 
        'cod_sessao_y','objeto_votacao_y']
df = df.drop(columns = cols)


# In[264]:


cols = df.columns.tolist()
print(cols)
# df_vp.head(1)


# In[265]:


cols = ['id_proposicao_x','data_votacao_x', 'hora_votacao_x','prop_data_hora_o','objeto_votacao_x',
        'tipo_proposicao_sigla_x','numero_proposicao_x', 'ano_proposicao_x',
        'resumo_votacao_x', 'cod_sessao_x','uf','nome','sigla_partido_x', 'voto',
        'sigla_partido_y','orientacao_partido',check_partido,]


df = df[cols]


# In[266]:


cols = df.columns.tolist()
print(cols)


# In[267]:


dic = {'id_proposicao_x':'id_proposicao', 'tipo_proposicao_sigla_x':'tipo_proposicao_sigla', 'numero_proposicao_x':'numero_proposicao', 
       'ano_proposicao_x':'ano_proposicao', 'resumo_votacao_x':'resumo_votacao', 'data_votacao_x':'data_votacao', 
       'hora_votacao_x':'hora_votacao', 'objeto_votacao_x':'objeto_votacao', 'cod_sessao_x':'cod_sessao', 'nome':'nome', 
       'sigla_partido_x':'sigla_partido', 'uf':'uf', 'voto':'voto', 'prop_data_hora_o':'prop_data_hora'}


dic['sigla_partido_y']='sigla_orientaçao_%s'%(partido)
dic['orientacao_partido']='voto_orientacao_%s'%(partido)
dic[check_partido] = check_partido


# In[268]:


df = df.rename(columns = dic)


# In[269]:


df.head()


# In[270]:


sigla_orientacao = 'sigla_orientaçao_%s'%(partido)
voto_orientacao = 'voto_orientacao_%s'%(partido)
check_partido = check_partido
cols=[sigla_orientacao,voto_orientacao,check_partido]

df_add = df[cols]


# In[273]:


df_add.head()


# In[274]:


df_save= pd.read_csv('../db/votacao_proposicao_votos_orientacao.csv')


# In[276]:


df_save = df_save.join(df_add)


# In[278]:


df_save.to_csv('../db/votacao_proposicao_votos_orientacao.csv', encoding='utf-8', index=False)


# In[ ]:





# In[ ]:


df= pd.read_csv('../db/votacao_proposicao_votos_orientacao.csv')


# In[ ]:


df

