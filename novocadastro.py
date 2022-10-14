from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pandas as pd
from encodings import utf_8
import mysql.connector
from mysql.connector import Error
from selenium.webdriver.common.keys import Keys



import time


class cadastrar():
   def cadastrar_clientes(self, caminho):
       service=Service(ChromeDriverManager().install())
       options = webdriver.ChromeOptions()
       options.add_argument('--headless')
      # navegador = webdriver.Chrome(service= service, options= options)
       navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
     #  navegador.get(f"file:///C:/Users/Usu%C3%A1rio/OneDrive/SAMUEL/PROGRAMACAO/Novo_Projeto/index.html") 
      # navegador.get(f"file:///C:/Users/Usu%C3%A1rio/Desktop/Novo_Projeto/index1.html")
       navegador.get(f"http://cnpj.info/" + str(caminho))
       time.sleep(5)
       result = navegador.find_element(By.XPATH, '/html/body').text
       novoresult =  result.splitlines()
       
       a1 = novoresult[5]
       nomedaempresa = a1[16:]
       a2 = novoresult[6]
       fantasia = a2[14:]
       a3 = novoresult[7]
       dataatividade = a3[22:]
       a4 = novoresult[11]
       capital = a4[15:]
       a5 = novoresult[13]
       opcao = a5[47:]
       endereco = novoresult[16]
       complemento= novoresult[17]
       cidade = novoresult[18]
       cep = novoresult[19]

    #  #   print(novoresult)
     #  busca = [s for s in novoresult if "Qualificação" in s]
       
       busca1 = [x for x in novoresult if "CPF***" in x]
       novosocio = []
       y = (len(busca1))
       if y != 1:
           for i in range(y):
               a = (busca1[i])
               b = a.split()
               c = len(b)
               d_ate_entrada = c-1
               e = b[1:d_ate_entrada]
               k = (len(e))-1
               
               l = ''.join(e[:k])
               
               novosocio.append(l)
               novosocio2 = list(zip(novosocio))
               socio = ', '.join(map(str, sorted(novosocio2)))
               #socio = zip(novosocio2)
               print(socio)
               
             #  print(socio)

       else:
          
           busca1 = [x for x in novoresult if "Nome" in x]
           y = (len(busca1))
           a7 = busca1[1]
           socio = a7[5:]
       
       a = novoresult.index("Atividades de negócios da empresa")
           
       g = a + 1
       
       h= novoresult[g]
       i = h[:9]
       chars = '. -'
       cnae= i.translate(str.maketrans('','', chars))
       
       self.novosdados = [nomedaempresa, fantasia, dataatividade, capital, opcao, endereco, complemento, cidade, cep, socio, cnae]
      # print(novosdados)
       
  # def tabelaclientes(self):
    #    colunas = ['NOMEDAEMPRESA', 'FANTASIA', 'DATADEINICIO', 'CAPITAL', 'DATADEOPCAO','ENDERECO', 'COMPLEMENTO', 'CIDADE', 'CEP', 'SOCIO', 'CNAE']
     #   dados = pd.DataFrame(columns=colunas)
        
      #  dados.loc[len(dados)] = self.novosdados
       

       
      

#é necessario verificar o caso de empresarios individuais que nao mostram quem é o sócio
    
       
#class AcessDataBase():
   def __init__(self, name = None):
        self._host='clientes1304.mysql.uhserver.com'
        self._user='samuel1304'
        self._passwd='@lb130488'
        self._database='tabelaclientes'
        self.con = None
        
   def _connect(self):
            self.con = mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._passwd,
            database=self._database
           )
            

   def close_connection(self):
        try:
            self.con.close()
               
        except:
            pass        

   def insert_table(self):
           
            cursor = self.con.cursor()
            
            valor = self.novosdados
            
            banco= "INSERT INTO Tabela_Clientes(NOMEDAEMPRESA, FANTASIA, dataatividade, CAPITAL, opcao,ENDERECO, COMPLEMENTO, CIDADE, CEP, SOCIO, CNAE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(banco, valor)
            cursor.close()
            print('inserido com sucesso')      
            self.con.commit()          

#def consulta_simples():

if __name__ == "__main__":
    caminho = '37128477000167'
    cd = cadastrar()
    cd.cadastrar_clientes(caminho)
    
   # db = AcessDataBase()
    cd._connect()
    cd.insert_table()
    cd.close_connection()
    print('conectado')
      
    