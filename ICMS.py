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


cnx = sqlite3.connect('system.db')
result = pd.read_sql_query("SELECT NCM, Percentagem_ICMS00,Percentagem_ICMS10, Percentagem_ICMS20 FROM Notas", cnx)


df = pd.DataFrame(result, columns = ['NCM','Percentagem_ICMS00', 'Percentagem_ICMS10', 'Percentagem_ICMS20'])

print (df)

a = ['10063021','22021000']
teste = []
#for linha in range(len(df)):
    #if df['NCM'].iloc[linha] in ['10063021','22021000']:
        #df['Percentagem_ICMS00'].iloc[linha] = '18'
def iter_pandas(x):
    if x['NCM'] in a:
        return '18'
df['Percentagem_ICMS00'] = df.apply(iter_pandas, axis=1)

#print(df)

def iter_pandas2(y):
    if y['NCM'] in ['04072100']:
        return '18'
df['Percentagem_ICMS10'] = df.apply(iter_pandas2, axis=1)

print(df)






