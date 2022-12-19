import sqlite3
from database import Database
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import numpy as np



class ICMS:
    
 #def iter_pandas2(y): 
    
    
    cnx = sqlite3.connect('system.db')
    variavel_b = "Cliente24722646000140saida"
    result_saida = pd.read_sql_query(f"""SELECT NCM, Percentagem_ICMS00,Percentagem_ICMS10, Percentagem_ICMS20 FROM {variavel_b}""", cnx)


    df_saida = pd.DataFrame(result_saida, columns = ['NCM','Percentagem_ICMS00', 'Percentagem_ICMS10', 'Percentagem_ICMS20'])
    #"Cliente01612795000151" "Cliente24722646000140entrada"
    
    variavel_a = "Cliente36966715000140entrada"
    result_entrada = pd.read_sql_query(f"""SELECT cnpj_emitente, NCM, CFOP, uf_emitente, valor_total_produto, Percentagem_ICMS00, Percentagem_ICMS10, Percentagem_ICMS20, CST_ICMS60, CST_ICMS70, Base_ICMS70, Percentagem_ICMS70, Valor_ICMS70 FROM {variavel_a}""", cnx)
    df_entrada = pd.DataFrame(result_entrada, columns= ['cnpj_emitente', 'NCM', 'CFOP','uf_emitente', 'valor_total_produto', 'Percentagem_ICMS00', 'Percentagem_ICMS10', 'Percentagem_ICMS20', 'CST_ICMS60', 'CST_ICMS70', 'Base_ICMS70','Percentagem_ICMS70', 'Valor_ICMS70'])
      
    
      
    
    def iter_pandas2(y):
       
       z = ['cnpj_emitente']
      
      
       for z in y:
           
           if z ==  y['cnpj_emitente']:
           
            rsresult = ['NÃO OPTANTE','Excluído do']
            service=Service(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
           # options.add_argument('--headless')
            navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
         #   navegador = webdriver.Chrome(service= service, options= options)
            
            navegador.get(f"http://cnpj.info/" + str(z))
            result=pd.read_html(navegador.find_element(By.ID, "content").get_attribute('innerHTML'))  
            nresult = np.array(result[0])
            novoresult = len(nresult) - 1
            nvresult = nresult[(novoresult-1):novoresult]
            for it in range(len(nvresult)):
                nxresult = nvresult[it]
                nzresult = str(nxresult[1])
                nyresult = nzresult[:11]
                
            
                base = pd.read_csv(r"C:\Users\Usuário\Desktop\Novo_Projeto\NCMDEFINITIVA.csv", encoding= 'UTF-8', sep= ';')
                
                base2 = pd.read_csv(r"C:\Users\Usuário\Desktop\Novo_Projeto\NCMREDUCAO.csv", encoding= 'UTF-8', sep= ';')
                variavel = []
                CFOP = ['5908','6908','5909','6909','6915', '5929','6929', '5915', '5916', '6915', '6916']
                ISENCAO = ['08104000','02006000','08109012','84386000','04039000','08021200','08109013','08109014']
                vnitem = []
                vnitem1 = []
                vnitem2 = []
                vnitem3 = []
                nitem = []
                sul = ['MG','SP','RJ','PR','RS','SC']
                var = []
                variavel = []
              
                if nyresult in rsresult:
                   
                            for item in base['NCM']:
                                vnitem.append(item)
                            for item1 in base['Ramo']:
                                vnitem1.append(item1)
                            for item2 in base['Porcentagem']:
                                vnitem2.append(item2)
                            for item3 in base['CEST']:
                                vnitem3.append(item3)
                                
                            if y['NCM'] in str(vnitem):
                                 a = vnitem.index(y['NCM'])
                                 
                                 print('TEM ST')
                                 
                                 for item in base2['NCM']:
                                    nitem.append(base2['NCM'])
                                 
                                 value_real = float(y['valor_total_produto'])
                                                        
                                 if y['NCM'] in str(nitem):
                                    
                                    print(nitem)
                                    print('TEM REDUCAO')
                                    if y['uf_emitente'] == 'DF':
                                        
                                        if y['CST_ICMS60'] == '60':
                                            
                                            #valorICMS = '60'
                                            variavel = '60'
                                            print(variavel)
                                        else:
                                            variavel = ['70', '18']+   [(vnitem2[a])] + [(vnitem3[a])]
                                            
                                            
                                            print(variavel) 
                                                               
                                    elif y['uf_emitente'] in sul:
                                            
                                            variavel = ['70', '7.00']+   [(vnitem2[a])] + [(vnitem3[a])]
                                            print(variavel)
                                    else:
                                        variavel = ['70', '12']+   [(vnitem2[a])] + [(vnitem3[a])]
                                      
                                        print(variavel)
                                    
                                            
                                 else:
                                    print('NÃO TEM REDUCAO')
                                    print (y['NCM']), print(nitem)
                                    if y['uf_emitente'] == 'DF':
                                           
                                            if y['CST_ICMS60'] == '60':
                                                
                                                variavel = '60'
                                                print(variavel)
                                            else:
                                                
                                                variavel = ['10', '18']+   [(vnitem2[a])] + [(vnitem3[a])]
                                                print(variavel)
                                                
                                                                                       
                                    elif y['uf_emitente'] in sul:
                                            variavel = ['70', '7.00']+   [(vnitem2[a])] + [(vnitem3[a])]
                                            print(variavel)
                                    else:
                                        variavel = ['70', '12.00']+   [(vnitem2[a])] + [(vnitem3[a])]
                                        print(variavel)
                                 
                                    
                            else:
                                for item in base2['NCM']:
                                    nitem.append(base2['NCM'])
                                if y['NCM'] in str(nitem):
                                        print('TEM REDUCAO SEM SUBSTITUICAO TRIBUTARIA')
                                        if y['uf_emitente'] == 'DF':
                                        
                                            variavel = ['20', '18']+   [(vnitem2[a])] + [(vnitem3[a])]  
                                            print(variavel)
                                                                                       
                                        elif y['uf_emitente'] in sul:
                                            variavel = '20.7'
                                            print(variavel)
                                        else:
                                            variavel = ['20', '12']+   [(vnitem2[a])] + [(vnitem3[a])]
                                            print(variavel)
                                            
                                else:
                                        print('NÃO TEM REDUCAO')
                                      
                                        
                                        if y['NCM'] in ISENCAO:
                                               
                                                variavel = '40'
                                                print(variavel)
                                        elif y['CFOP'] in CFOP:
                                                
                                                variavel = '41'
                                                print(variavel)
                                                
                                        else:
                                            if y['uf_emitente'] == 'DF':
                                                
                                                variavel = '18'
                                                print(variavel)
                                                
                                                                                       
                                            elif y['uf_emitente'] in sul:
                                                variavel = '7'
                                                print(variavel)
                                           
                                            
                                            else:
                                                variavel = '12'
                                                print(variavel)
                                 
                                        
                else:
                    
                    if y['NCM'] in ISENCAO:
                            variavel = '40'
                            print(variavel)
                    elif y['CFOP'] in CFOP:
                            variavel = '41'
                            print(variavel)
                    else:
                        for item in base['NCM']:                            
                            if y['NCM'] in item:
                                if y['uf_emitente'] == 'DF':
                                    if y['CST_ICMS60'] == '60':
                                        variavel = '60'
                                        print(variavel)
                                    else:
                                        variavel = '10.18'
                                        print(variavel)
                                elif y['uf_emitente'] in sul:
                                    variavel = '10.7'
                                    print(variavel)
                                else:
                                    variavel = '10.12'
                                    print(variavel)
                            else:
                                variavel = 'input valor'
                                print(variavel)
                                    
                                
            return variavel
    
    #if __name__ == "__main__":
         
    
    
    df_entrada['NOVACOLUNA'] = df_entrada.apply(iter_pandas2, axis=1)
   
   
    for s in df_entrada.iterrows():
          
        
        indice = s[0]
        
        k = df_entrada.iloc[indice, 13]
    
        if k[0] == '70':
            df_entrada.iat[indice, 11] = k[1]
            cursor = cnx
            cursor.execute (f"""UPDATE 'Cliente36966715000140entrada' SET CST_ICMS70 = {k[1]} WHERE ID = {indice + 1}""" )
            cnx.commit()      
            print('atualizado com sucesso') 
           
         
    
        #    print(df_entrada.iloc[indice, 13])
         #   if df_entrada.iloc[indice, 13] == '70':
          #      print(indice), print('ver1')
           #     df_entrada.iat[indice, 10] = 18
            #    df_entrada.iat[(len(s)-1),10]= df_entrada['valor_total_produto']* 0.20 * 1.6666
             #   df_entrada.iat[(len(s)-1), 11]= df_entrada['valor_total_produto']* 0.20 * 1.6666 * 0.18 - df_entrada['valor_total_produto'] * 0.20 * 1.6666
    print(df_entrada)
          #1  elif df_entrada.iloc[indice, 12] == '5':
         #1       print(indice), print('ver2')
          #1      df_entrada.iat[indice, 10] = 12
          #      df_entrada.iat[(len(x)-1),10]= df_entrada['valor_total_produto']* 0.20 * 1.6666
           #     df_entrada.iat[(len(x)-1), 11]= df_entrada['valor_total_produto']* 0.20 * 1.6666 * 0.12 - df_entrada['valor_total_produto'] * 0.20 * 1.6666
              #  print(df_entrada)
          #1  else:
         #1      print('deu erro')
        #1    print(df_entrada)
        
               
        
    #df_entrada = pd.DataFrame(result_entrada, columns= ['cnpj_emitente', 'NCM', 'uf_emitente', 'valor_total_produto','Percentagem_ICMS00', 'Percentagem_ICMS10','Percentagem_ICMS20', 'CST_ICMS60', 'CST_ICMS70']) 
   # df_entrada['Percentagem_ICMS20'].to_list() 
       # for x in (list(y)):
         # for z in range((y[x])):
          #  print(x) 
           # if y == 3:
               
               # novaentrada = z[x][y]
               # df_entrada.iat[,1] =  
               # print(z)
                
          
    
    
        
            
                
    #class impressao():
        #def recalculo(agora): 
    
           # df_entrada.to_excel('entrada.xlsx')
         #  print(agora['Percentagem_ICMS10'])
    
       # df_saida['Percentagem_ICMS10'] = df_saida.apply(iter_pandas2, axis=1)
   
     
   # print(df_entrada)
#1    print('fim')