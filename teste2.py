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
  

leitor= pd.read_csv(r"C:\Users\Usuário\OneDrive\SAMUEL\PROGRAMACAO\SISTEMA_NCM\SISTEMA_NCM.csv", encoding= 'UTF-8', sep= ';')
  
#colunas = ['NCM', 'Descrição', 'Porcentagem', 'CEST']
colunas = ['NCM', 'Descrição']
dados = pd.DataFrame(columns=colunas)
for linha in leitor['NCM']:
    
        novalinha = (linha[:10])
        print(novalinha)
   
        navegador.get("https://www.iobonline.com.br/pages/coreonline/coreonlineComparativoNcm.jsf")
        time.sleep(5)
      
        navegador.find_element(By.XPATH, '//*[@id="frm-comparativo:txtNcm"]').send_keys(novalinha)
        navegador.find_element(By.XPATH, '//*[@id="frm-comparativo:j_id13"]').click()
       
        time.sleep(5)
#/html/body/section[2]/div/div[4]/table[1]/tbody/tr[2]/td[2]/button
        result=pd.read_html(navegador.find_element(By.ID, 'table-result').get_attribute('innerHTML'))
        novoresult = result[0]
        nvresult = novoresult[1]
        nresult = nvresult[2]
        
        novodados = [novalinha, nresult]
        predados = dados.dropna(axis=0, how='any')
                       
        dados.loc[len(dados)] = novodados
                          
                        
        print(predados)
        predados.to_csv('GENERONCM.csv', sep=';' )
        
        
        
       
                 

                          
                        
                          
        #predados.to_csv('TABELANCM.csv', sep=';' )
    
            # /html/body/section[2]/div/div[4]/div[2]/div[2]  
              
           
            