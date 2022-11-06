from encodings import utf_8
from msilib.schema import Error
import os
from xml.dom.minidom import Document
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
import requests as re
from bs4 import BeautifulSoup
import numpy as np
import re
import csv
import math


navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "https://www.iobonline.com.br/vitrine-ferramentas"
navegador.get(link)
time.sleep(10)

navegador.find_element(By.XPATH, '/html/body/section[1]/header/header/div[2]/div[2]/div[2]/a').click()    
time.sleep(5)
lista_abas = navegador.window_handles[0]
navegador.switch_to.window(lista_abas)
navegador.find_element(By.XPATH, '//*[@id="txtPassword"]').send_keys('alb130488')
navegador.find_element(By.XPATH,'//*[@id="txtLogin"]').send_keys('ADRIANA13')
time.sleep(5)
navegador.find_element(By.XPATH,'//*[@id="form-user"]/div/table/tbody/tr[4]/td/button').click()
        
time.sleep(10)
  

leitor= pd.read_csv(r"C:\Users\Usuário\OneDrive\SAMUEL\PROGRAMACAO\SISTEMA_NCM\CONSULTANCM2.csv", encoding= 'UTF-8', sep= ';')
  
#colunas = ['NCM', 'Descrição', 'Porcentagem', 'CEST']
colunas = ['NCM', 'Descrição']
dados = pd.DataFrame(columns=colunas)
for linha in leitor['NCM']:
    
        novalinha = (linha[:10])
        print(novalinha)
   
        navegador.get("https://www.iobonline.com.br/ncm")
        time.sleep(5)
      
        navegador.find_element(By.XPATH, '//*[@id="txtBusca"]').send_keys(novalinha)
        navegador.find_element(By.XPATH, '//*[@id="sclUFs"]/option[8]').click()
        navegador.find_element(By.XPATH,'//*[@id="tools"]/div/form/div[3]/button').click()
        time.sleep(5)
#/html/body/section[2]/div/div[4]/table[1]/tbody/tr[2]/td[2]/button

        opcao = navegador.find_elements(By.XPATH, '//*[@id="consulting"]')
        lista = navegador.find_elements(By.XPATH, '//*[@id="consultingEX"]')
        #if len(lista)>0:
        superlista = opcao + lista

        #def analisar():
        for item in superlista:
            item.click()

           # time.sleep(2)
        
            try:
              if navegador.find_element(By.XPATH, '//*[@id="institutes"]/div/div[4]') != "":
                  navegador.find_element(By.XPATH, '//*[@id="institutes"]/div/div[4]').click()   
                  
                 # time.sleep(2)
                  
                  substtrib = navegador.find_elements(By.XPATH, '//*[@id="icms-list"]')
                  
                  
                #novodf = []
                  for elemento1 in substtrib:
                    if "Substituição Tributária" in elemento1.text:
                      navegador.execute_script(f"window.scrollTo(0, -100)")
                      navegador.execute_script(f"window.scrollTo(0, 1000)")  
                      elemento1.click()

                    time.sleep(2)
                    
              
              #navegador.find_element(By.XPATH, '//*[@id="subs-table"]/tbody[1]/tr[1]/td[4]')
                
        
              result=pd.read_html(navegador.find_element(By.ID, "boxResultTributo").get_attribute('innerHTML'))  
              
              novoresult = np.array(result)

              for i in range(len(novoresult)):
                      for j in range(len(novoresult[i])):
                          valor = novoresult[i][j]
                    
                          m1 = valor[0]
                            
                         # m3 = valor[3]
                        #  m4 = valor[4]
                  
                          descricao =  str(np.array(m1).tolist()).strip('')
                           
                        #  porcentagem = np.array(m3)
  
                         # cest = np.array(m4).tolist()
             
                        #  novosdados = [novalinha, descricao, porcentagem, cest]
                          novosdados = [novalinha, descricao]
                          predados = dados.dropna(axis=0, how='any')
                       
                          dados.loc[len(dados)] = novosdados
                          
                        
                          print(predados)
                          predados.to_csv('TABELANCM.csv', sep=';' )
    
            # /html/body/section[2]/div/div[4]/div[2]/div[2]  
              
           
            except:
                print('Não se aplica')
            time.sleep(5)
            try:
              navegador.find_element(By.XPATH,'/html/body/div[4]/i').click()
              time.sleep(5)
  
              navegador.find_element(By.XPATH, '/html/body/section[2]/div/div[4]/div[1]/button').click() 
     
              time.sleep(10)
            except:
                 # if len(superlista) > 1:
                     #   analisar()
                 # else:
                       navegador.get("https://www.iobonline.com.br/vitrine-ferramentas")
            
   

navegador.find_element(By.XPATH, '//*[@id="toolbar"]/div/div[3]/a').click()
time.sleep(14)
#ActionChains(navegador).move_to_element(a).perform()
