from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pandas as pd
from encodings import utf_8
import numpy as np
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
       
       nomedaempresa = novoresult[5]
       fantasia = novoresult[6]
       dataatividade = novoresult[7]
       capital = novoresult[11]
       opcao = novoresult[13]
       endereco = novoresult[16]
       complemento= novoresult[17]
       bairro = novoresult[18]
       cep = novoresult[19]
       telefone = novoresult[22]
    #   print(novoresult)
     #  busca = [s for s in novoresult if "Qualificação" in s]
       
       busca1 = [x for x in novoresult if "CPF***" in x]
       y = (len(busca1))
       if y != 1:
           for i in range(y):
               a = (busca1[i])
               b = a.split()
               c = len(b)
               d_ate_entrada = c-1
               e = b[1:d_ate_entrada]
               socio = (len(e))-1
               print(e[socio:])
               print(e[:socio])
       else:
          
           busca1 = [x for x in novoresult if "Nome" in x]
           y = (len(busca1))
           print(busca1[1])

#é necessario verificar o caso de empresarios individual que nao mostram quem é o sócio
def tabelaclientes():
    colunas = ['NCM', 'Descrição']
    dados = pd.DataFrame(columns=colunas)  



                

#def consulta_simples():

if __name__ == "__main__":
    caminho = '11320004000173'
    cd = cadastrar()
    cd.cadastrar_clientes(caminho)
  
    