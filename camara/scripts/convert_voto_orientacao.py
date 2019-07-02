#!/usr/bin/env python
# coding: utf-8

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


def join_prop_data_hora():

  df_o= pd.read_csv('../db/votacao_proposicao_orientacao.csv')
  df_v= pd.read_csv('../db/votacao_proposicao.csv')


  df_vp=df_v.copy()

  df_op=df_o.copy()

  df_op_dp = pd.DataFrame()
  df_vp_dp = pd.DataFrame()

  df_op_dp['prop'] = df_op['id_proposicao']
  df_vp_dp['prop'] = df_vp['id_proposicao']

  df_op_dp['data_hora_o'] = pd.to_datetime(df_op['data_votacao'] + ' ' + df_op['hora_votacao'])
  df_vp_dp['data_hora_v'] = pd.to_datetime(df_vp['data_votacao'] + ' ' + df_vp['hora_votacao'])


  df_op['prop_data_hora_o'] = df_op_dp.apply(lambda x: ' '.join(x.astype(str)), axis=1)
  df_vp['prop_data_hora_o'] = df_vp_dp.apply(lambda x: ' '.join(x.astype(str)), axis=1)



  df_vp.head(2)


  df_op.to_csv('../db/votacao_proposicao_orientacao_prop_data_hora.csv', encoding='utf-8', index=False)
  df_vp.to_csv('../db/votacao_proposicao_prop_data_hora.csv', encoding='utf-8', index=False)

  print('concatenated (;\n')












def merge_votos_orientacao(part):

  partido = part

  df_o= pd.read_csv('../db/votacao_proposicao_orientacao_prop_data_hora.csv')
  df_v= pd.read_csv('../db/votacao_proposicao_prop_data_hora.csv')


  df_vp=df_v.copy()
  cols=['ide_cadastro','data_captura','url_captura']
  df_vp = df_vp.drop(columns = cols)



  df_op=df_o.copy()
  cols=['data_captura','url_captura','numero_captura']
  df_op = df_op.drop(columns = cols)

  print('Numero de partidos nas proposições Orientadas', len(list(df_op['sigla_partido'].unique())))
  print('Numero de proposições Orientadas', len(list(df_op['prop_data_hora_o'].unique())))


  df_op = df_op[df_op['sigla_partido']==partido]
  print('Proposiçoes Orientadas Pelo Partido %s'%(partido),len(list(df_op['prop_data_hora_o'] )))


  df_vp = df_vp.rename({'prop_data_hora_p':'prop_data_hora_o'})


  check_partido = 'check_%s'%(partido)
  df_op[check_partido]=1


  cols=['prop_data_hora_o']
  df = pd.merge(df_vp , df_op, on = cols ,how = 'left')


  df.describe()



  cols = df.columns.tolist()




  cols = [ 'id_proposicao_y', 'tipo_proposicao_sigla_y', 'numero_proposicao_y', 
          'ano_proposicao_y', 'resumo_votacao_y', 'data_votacao_y', 'hora_votacao_y', 
          'cod_sessao_y','objeto_votacao_y']
  df = df.drop(columns = cols)



  cols = df.columns.tolist()


  cols = ['id_proposicao_x','data_votacao_x', 'hora_votacao_x','prop_data_hora_o','objeto_votacao_x',
          'tipo_proposicao_sigla_x','numero_proposicao_x', 'ano_proposicao_x',
          'resumo_votacao_x', 'cod_sessao_x','uf','nome','sigla_partido_x', 'voto',
          'sigla_partido_y','orientacao_partido',check_partido,]


  df = df[cols]


  cols = df.columns.tolist()


  dic = {'id_proposicao_x':'id_proposicao', 'tipo_proposicao_sigla_x':'tipo_proposicao_sigla', 'numero_proposicao_x':'numero_proposicao', 
         'ano_proposicao_x':'ano_proposicao', 'resumo_votacao_x':'resumo_votacao', 'data_votacao_x':'data_votacao', 
         'hora_votacao_x':'hora_votacao', 'objeto_votacao_x':'objeto_votacao', 'cod_sessao_x':'cod_sessao', 'nome':'nome', 
         'sigla_partido_x':'sigla_partido', 'uf':'uf', 'voto':'voto', 'prop_data_hora_o':'prop_data_hora'}


  dic['sigla_partido_y']='sigla_orientaçao_%s'%(partido)
  dic['orientacao_partido']='voto_orientacao_%s'%(partido)
  dic[check_partido] = check_partido


  df = df.rename(columns = dic)


  df.to_csv('../db/votacao_proposicoes_votos_orientacao_%s.csv'%(partido), encoding='utf-8', index=False)

  sigla_orientacao = 'sigla_orientaçao_%s'%(partido)
  voto_orientacao = 'voto_orientacao_%s'%(partido)
  check_partido = check_partido
  cols=[sigla_orientacao,voto_orientacao,check_partido]

  df_add = df[cols]





  df_save= pd.read_csv('../db/votacao_proposicoes_votos_orientacao.csv')



  df_save = df_save.join(df_add)
  
  cols = df_save.columns.tolist()
  print(cols)

  df_save.to_csv('../db/votacao_proposicao_votos_orientacao.csv', encoding='utf-8', index=False)

  print('merged ;)\n')