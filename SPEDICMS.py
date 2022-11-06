import sqlite3
from datetime import datetime
import pandas as pd


dados = datetime.now()

#def tabela_principal(self):        
cn = sqlite3.connect('system.db')
result0150 =  pd.read_sql_query("SELECT nome_emitente, cnpj_emitente, inscricao_emitente,  logradouro_emitente, numero_emitente, complemento_emitente, bairro_emitente, codigo_municipio_emitente FROM Cliente24722646000140entrada WHERE nfe != ''", cn)

df = pd.DataFrame(result0150, columns = ['nome_emitente','codigo_pais','cnpj_emitente', 'inscricao_emitente','codigo_municipio_emitente', 'logradouro_emitente', 'numero_emitente', 'complemento_emitente', 'bairro_emitente'])


df = df.drop_duplicates(subset ="nome_emitente",keep = 'first')
df.insert(0, 'codigo_cliente', range(880, 880 + len(df)))

df.loc[df['codigo_pais'] != '','codigo_pais'] = '1058'


novodf= df['nome_emitente'].str.replace(' ', '_')

novodf1 = df['logradouro_emitente'].str.replace(',', '.')
df.drop(columns=['nome_emitente','logradouro_emitente'], inplace= True)


df.insert(1,'nome_emitente', novodf)
df.insert(5,'logradouro_emitente',novodf1)

novodf2 = df['nome_emitente'].str.replace(',', '_')

novodf3 = df['logradouro_emitente'].str.replace(' ', '_')
df.drop(columns=['nome_emitente','logradouro_emitente'], inplace= True)


df.insert(1,'nome_emitente', novodf2)
df.insert(5,'logradouro_emitente',novodf3)


df2 = df.values.tolist()



for x in range(len(df2)):
      arquivo = open('teste.txt', 'a')
      arquivo.writelines(str(df2[x])+'\n')
arquivo = open('teste.txt', 'r')
novoarq = arquivo.readlines()

print('chegou aqui')
arquivo = open('teste.txt', 'w')


for i in range(len(novoarq)):
      for j in range(len(novoarq[i])):
        novoarquivo =novoarq[i][j]
       # if novoarquivo == ",":
        novoarquivo= novoarquivo.strip()
        novoarquivo = novoarquivo.replace('[','|0150|')
        novoarquivo = novoarquivo.replace(']','|\n')
        novoarquivo = novoarquivo.replace('_',' ')
        
        novoarquivo = novoarquivo.removesuffix("'")
       
        arquivo.write(str(novoarquivo.replace(",","|")))
       
