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
      # navegador.get(f"file:///C:/Users/Usu%C3%A1rio/OneDrive/SAMUEL/PROGRAMACAO/Novo_Projeto/index.html") 
       navegador.get(f"http://cnpj.info/" + str(caminho))
       time.sleep(5)
       result = navegador.find_element(By.XPATH, '/html/body').text
       novoresult =  result.splitlines()
       nomedaempresa = novoresult[5]
       print(nomedaempresa[16:])





                

#def consulta_simples():

if __name__ == "__main__":
    caminho = '05975390000139'
    cd = cadastrar()
    cd.cadastrar_clientes(caminho)
  
    