import sqlite3
from datetime import datetime
import pandas as pd

dados = datetime.now()

#def tabela_principal(self):        
cn = sqlite3.connect('system.db')
result0150 =  pd.read_sql_query("SELECT nome_emitente, cnpj_emitente, inscricao_emitente, codigo_municipio_emitente, logradouro_emitente, numero_emitente, complemento_emitente, bairro_emitente FROM Cliente24722646000140entrada WHERE nfe != ''", cn)
df = pd.DataFrame(result0150, columns = ['nome_emitente','codigo_pais','cnpj_emitente', 'inscricao_emitente','codigo_municipio_emitente' 'logradouro_emitente', 'numero_emitente', 'complemento_emitente', 'bairro_emitente'])


df = df.drop_duplicates(subset ="nome_emitente",keep = 'first')


df.loc[df['codigo_pais'] != '','codigo_pais'] = '1058'
    #vamos transformar cada linha do dataframe numa lista e inserir no codigo 0150 do txt  



#df.loc[df['Municipio_emitente'] == [leitor['Nome Municipio']],'Municipio_emitente'] = leitor['Codigo Municipio Completo']

 

arquivo = open('teste.txt', 'a')
arquivo.writelines(str(df))
#result0150 = result0150.values.tolist()
#temp = set()
#res0150 = [el for el in result0150 if not(tuple(el) in temp or temp.add(tuple(el)))] 
#arquivo = open('teste.txt', 'a')
#arquivo.writelines(str(res0150)+"|")
#for x in range(len(res0150)):
      # for y in range(len(res0150[x])):
             # if y = 0
           
            #  arquivo = open('teste.txt', 'a')
             # arquivo.write(str(res0150[x][y])+"|")
#arquivo = open('teste.txt', 'r')
#unica_string = arquivo.read()
#arquivo.close()
#print(unica_string)
#with open('teste.txt','r') as arquivo:
   #for valor in arquivo:
        #  print(valor[0])
       

     #estou achando a primeira string entao preciso achar a string | e acrescentar os codigos que preciso     

#for x in range(len(res0150)):
  #  print(x)
 #   novox = res0150[x]
  #  for y in range(len(novox)):
        # print(res0150[x][0])
      #  print(result[x][2])
#print(res0150[0])
              
    #print(len(result))
 #   novoresult = result[x]+"|"
  #  print(novoresult)

#arquivo = open('teste.txt', 'a')
#arquivo.write(str(res0150)+"|")







