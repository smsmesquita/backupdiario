from cmath import nan
from msilib.schema import Condition
from operator import index
from random import choices
import sqlite3
from mysqlx import Result, RowResult
import numpy as np 
import pandas
from database import Database
import pandas as pd
from turtle import pos


class ICMS:
    
    
    
    
#for linha in range(len(df)):
    #if df['NCM'].iloc[linha] in ['10063021','22021000']:
        #df['Percentagem_ICMS00'].iloc[linha] = '18'
    cnx = sqlite3.connect('system.db')
    variavel_b = "Cliente24722646000140saida"
    result_saida = pd.read_sql_query(f"""SELECT NCM, Percentagem_ICMS00,Percentagem_ICMS10, Percentagem_ICMS20 FROM {variavel_b}""", cnx)


    df_saida = pd.DataFrame(result_saida, columns = ['NCM','Percentagem_ICMS00', 'Percentagem_ICMS10', 'Percentagem_ICMS20'])
    
    variavel_a = "Cliente24722646000140entrada"
    result_entrada = pd.read_sql_query(f"""SELECT NCM, Percentagem_ICMS00,Percentagem_ICMS10, Percentagem_ICMS20 FROM {variavel_a}""", cnx)


    df_entrada = pd.DataFrame(result_entrada, columns = ['NCM','Percentagem_ICMS00', 'Percentagem_ICMS10', 'Percentagem_ICMS20'])
    
    def iter_pandas2(y):
        base = pd.read_csv(r"C:\Users\Usuário\Desktop\Novo_Projeto\NCMDEFINITIVA.csv", encoding= 'UTF-8', sep= ';')
       # nbase = base['NCM']
       # nobase = (str(nbase)).replace('.','')
        #PRECISO RESOLVER ESSE PROBLEMA: O SISTEMA NÃO PERMITE QUE EU MUDE A BASE PARA UMA NOVA BASE SEM '.' E TAMBÉM NÃO ACEITAR FAZER ITERABLE SE EU COLOCAR O NCM DO CSV NO MODO PERSONALIZADO
        for item in base['NCM']:
            if y['NCM'] in item:
                return '11'
    df_entrada['Percentagem_ICMS10'] = df_entrada.apply(iter_pandas2, axis=1)
    df_saida['Percentagem_ICMS10'] = df_saida.apply(iter_pandas2, axis=1)
    print(df_entrada)
 #   print('fez entrada')
   # print(df_saida)
 #   print('fez saida')

# 1 verificar se é de entrada ou saida as notas
#1.1 se for de entrada 
#1.1.1 verificar substituicao tributaria do produto (se não foi recolhido recolher porque não será preciso conferir se tem que sair com ST(1.2.1))
#1.1.1.1 Verificar os casos de dispensa de ST para fabrica
#1.1.2 verificar se o fornecedor é do Simples para zerar o icms
#1.1.3 conferir se o GTIN do produto está com outro NCM
#1.1.4 conferir se o produto entrou com redução ou isencao
#1.2 se for de saida:
#1.2.1 conferir se o produto deve sair com ST 
#1.2.1.1 Se o produto é do fabricante, não teve entrada(porque foi transformado) cobrar ST
#1.2.1.2 Se o produto entrou com 010 sair com 060
#1.2.2 conferir se o produto tem redução
#1.2.3 conferir se o produto é isento

