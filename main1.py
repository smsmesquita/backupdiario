from os import access, name
import sqlite3
from turtle import pd
from xml.etree.ElementTree import XML
from PySide2.QtWidgets import (QApplication, QFileDialog, QMainWindow, QWidget, QMessageBox, QTableView, QTreeWidget, QTreeWidgetItem)
from database import Database
from ui_login import Ui_Login
from ui_cadastro import *
import sys
from ui_sistema import Ui_MainWindow
from xml_files import Read_xml
import pandas as pd
from PySide2 import QtCore, QtGui
from PyQt5 import QtGui
import re
import mysql
from novocadastro import *
import mysql.connector
from mysql.connector import Error



class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Login do Sistema')
  
        self.pushButton_2.clicked.connect(self.open_system)
        self.pushButton_4.clicked.connect(self.open_sistemacadastro)
        self.pushButton_4.clicked.connect(lambda: print('botao 4 foi apertado'))
        
        self.pushButton_2.clicked.connect(lambda: print('botao 2 foi apertado'))
        #self.pushButton_3.clicked.connect(lambda: print('botao 3 foi apertado'))
        
        
    
    def open_system(self):
        #senha = self.textEdit.toPlainText()
        #if senha == "123":
        self.w = MainWindow()
        self.w.show()
        self.close()
           
    def open_sistemacadastro(self):
        self.w = NovoMainWindow()
        self.w.show()
        self.close()
        
        
                    

        
class MainWindow(QMainWindow, Ui_MainWindow,QTreeWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Sistema') 
        
    #appIcon = QtGui.QIcon('C:\Users\Usuário\OneDrive\SAMUEL\PROGRAMACAO\xml_teste\imagem'
    #self.SetWindowIcon(appIcon)  
       
       
        
        self.btn_open.clicked.connect(self.open_path)
        
        
        
        self.pushButton_12.clicked.connect(self.excel_files)
        
    def open_path(self):
        self.path = QFileDialog.getExistingDirectory (self , str("Open Directory"),"/home",
                                                     QFileDialog.ShowDirsOnly)
                                                        #QFileDialog.DontResolveSymlinks)
                                                     
        
        
                                           
                                                     
        self.txt_file.setText(self.path)
        
        self.btn_importar.clicked.connect(self.import_xml_files)
        
     
         
        
    def import_xml_files(self):
        xml = Read_xml(self.txt_file.text())
        all = xml.all_files()
        self.progressBar.setMaximum(len(all))
             
   
            
        db = Database()
        
        db.conecta()
        
         
        cont = 1
            
        for i in all:
            self.progressBar.setValue(cont)
            fullDataSet = xml.nfe_data(i)
           # self.tabela_principal() - resolvi comentar essa tabela porque estava conflitando com o criar tabela nota
            db.create_table_nfe()
            db.insert_data(fullDataSet)
          
            
            cont +=1
 
              
            # ATUALIZA A TABELA   
            
            #msg = QMessageBox()
            #msg.setIcon(QMessageBox.Information)
            #msg.setWindowTitle("Importação XML")
            #msg.setText("Importação Concluída")
            #msg.exec_()
            self.progressBar.setValue(0)
     
            db.close_connection            
            
            
            
        
    def tabela_principal(self):        
        cn = sqlite3.connect('system.db')
        result =  pd.read_sql_query("SELECT nfe, data_emissao, cnpj_emitente, nome_emitente,chave_de_acesso, produto, NCM, CFOP, valor_produto FROM Notas WHERE nfe != ''", cn)
        result = result.values.tolist()
        self.x = ""
        
      #  for i in result:
         #   if i[0]== self.x:
          #      QTreeWidgetItem(self.campo, i)
           # else:
               # self.campo = QTreeWidgetItem(self.tabela_geral, i)
               # self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)
                
                
                
           # self.x = i[0]
            
          #  self.tabela_geral.setSortingEnabled(True)
        
      #  for i in range(1,49):
       #     self.tabela_geral.resizeColumnToContents(i)
            
    
    #def update_filter(self, s):
        #s = re.sub("[\W]"+, "", s)
        #filter_str = 'Nfe LIKE "%{}%"'.format(s)
        #self.model.setFilter(filter_str) 
        
    def excel_files(self):
        cnx = sqlite3.connect('system.db')
        result = pd.read_sql_query("SELECT * FROM Notas", cnx)
        result.to_excel("Resumo.xlsx",sheet_name= 'Notas', index=False)
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Relatorio")
        msg.setText("Gerado com sucesso")
        msg.exec_()
        

                
class NovoMainWindow(QMainWindow, Ui_MainWindow2,QTreeWidget):
    def __init__(self):
        super(NovoMainWindow, self).__init__()
        db = Database()
        
        db.conecta()
     
        
        self.setupUi(self)
        self.setWindowTitle('Sistema') 
        
        self.pushButton_11.clicked.connect(self.cadastro)
        self.tabela_saida()
      #  self.criador_tabela_geral()
        self.pushButton_11.clicked.connect(self.criador_tabela_geral)
        self.pushButton_11.clicked.connect(self.criador_tabela_analitica)
        
   
        self._host='clientes1304.mysql.uhserver.com'
        self._user='samuel1304'
        self._passwd='@lb130488'
        self._database='tabelaclientes'
        self.con = None
        
 
    def cadastro(self):
        
        caminho= self.lineEdit.text()
        cadastrar.cadastrar_clientes(self, caminho)
        
        cadastrar._connect(self)
        
        cadastrar.insert_table(self)
        cadastrar.close_connection(self)
        
      
    def criador_tabela_geral(self):
        self._host='clientes1304.mysql.uhserver.com'
        self._user='samuel13'
        self._passwd='@lb130488'
        self._database='clientes1304'
        self.con = None        
        
        self.con = mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._passwd,
            database=self._database
           )
        titulo = self.lineEdit.text()
        cursor = self.con.cursor()
        print('chegou')
        cursor.execute (f"""
                CREATE TABLE IF NOT EXISTS {str('Cliente')+ titulo} (
                Idtabela int(11) NOT NULL auto_increment,
                nfe TEXT NOT NULL,
                serie TEXT NOT NULL,
                data_emissao TEXT NOT NULL,
                cnpj_emitente TEXT NOT NULL,
                nome_emitente TEXT NOT NULL,
                logradouro_emitente TEXT NOT NULL, 
                numero_emitente TEXT NOT NULL,
                complemento_emitente TEXT NOT NULL, 
                bairro_emitente TEXT NOT NULL, 
                codigo_municipio_emitente TEXT NOT NULL, 
                Municipio_emitente TEXT NOT NULL, 
                uf_emitente TEXT NOT NULL, 
                cep_emitente TEXT NOT NULL, 
                cod_pais_emitente TEXT NOT NULL, 
                pais_emitente TEXT NOT NULL, 
                chave_de_acesso TEXT NOT NULL, 
                codigo_barras TEXT NOT NULL, 
                produto TEXT NOT NULL, 
                NCM TEXT NOT NULL, 
                CFOP TEXT NOT NULL, 
                unidade_comercial TEXT NOT NULL, 
                quantidade_comercial TEXT NOT NULL, 
                valor_unidade_comercial TEXT NOT NULL, 
                valor_total_produto TEXT NOT NULL, 
                quantidade_produto TEXT NOT NULL, 
                valor_produto TEXT NOT NULL, 
                CST_ICMS00 TEXT NOT NULL,
                cod_origem00 TEXT NOT NULL,
                Base_ICMS00 TEXT NOT NULL, 
                Percentagem_ICMS00 TEXT NOT NULL, 
                Valor_ICMS00 TEXT NOT NULL,
                CST_ICMS10 TEXT NOT NULL,
                cod_origem10 TEXT NOT NULL,
                Base_ICMS10 TEXT NOT NULL, 
                Percentagem_ICMS10 TEXT NOT NULL, 
                Valor_ICMS10 TEXT NOT NULL,
                CST_ICMS20 TEXT NOT NULL,
                cod_origem20 TEXT NOT NULL,
                Base_ICMS20 TEXT NOT NULL, 
                Percentagem_ICMS20 TEXT NOT NULL, 
                Valor_ICMS20 TEXT NOT NULL,
                CST_ICMS30 TEXT NOT NULL,
                CST_ICMS40 TEXT NOT NULL,
                CST_ICMS41 TEXT NOT NULL,
                CST_ICMS50 TEXT NOT NULL,
                CST_ICMS51 TEXT NOT NULL,
                CST_ICMS60 TEXT NOT NULL,
                CST_ICMS70 TEXT NOT NULL,
                CST_ICMS90 TEXT NOT NULL, 
                    
                
                
                PRIMARY KEY(Idtabela)
                );                            
              
                """)
           
    def criador_tabela_analitica(self):
       
        
        db = Database()
        
        db.conecta()
        self.connection = sqlite3.connect('system.db')
        
        cursor = self.connection.cursor()
               
        titulo1 = self.lineEdit.text()
        
        cursor.execute (f"""
                CREATE TABLE IF NOT EXISTS {str('Cliente')+ titulo1} (
                Idtabela int(11) NOT NULL,
                nfe TEXT NOT NULL,
                serie TEXT NOT NULL,
                data_emissao TEXT NOT NULL,
                cnpj_emitente TEXT NOT NULL,
                nome_emitente TEXT NOT NULL,
                logradouro_emitente TEXT NOT NULL, 
                numero_emitente TEXT NOT NULL,
                complemento_emitente TEXT NOT NULL, 
                bairro_emitente TEXT NOT NULL, 
                codigo_municipio_emitente TEXT NOT NULL, 
                Municipio_emitente TEXT NOT NULL, 
                uf_emitente TEXT NOT NULL, 
                cep_emitente TEXT NOT NULL, 
                cod_pais_emitente TEXT NOT NULL, 
                pais_emitente TEXT NOT NULL, 
                chave_de_acesso TEXT NOT NULL, 
                codigo_barras TEXT NOT NULL, 
                produto TEXT NOT NULL, 
                NCM TEXT NOT NULL, 
                CFOP TEXT NOT NULL, 
                unidade_comercial TEXT NOT NULL, 
                quantidade_comercial TEXT NOT NULL, 
                valor_unidade_comercial TEXT NOT NULL, 
                valor_total_produto TEXT NOT NULL, 
                quantidade_produto TEXT NOT NULL, 
                valor_produto TEXT NOT NULL, 
                CST_ICMS00 TEXT NOT NULL,
                cod_origem00 TEXT NOT NULL,
                Base_ICMS00 TEXT NOT NULL, 
                Percentagem_ICMS00 TEXT NOT NULL, 
                Valor_ICMS00 TEXT NOT NULL,
                CST_ICMS10 TEXT NOT NULL,
                cod_origem10 TEXT NOT NULL,
                Base_ICMS10 TEXT NOT NULL, 
                Percentagem_ICMS10 TEXT NOT NULL, 
                Valor_ICMS10 TEXT NOT NULL,
                CST_ICMS20 TEXT NOT NULL,
                cod_origem20 TEXT NOT NULL,
                Base_ICMS20 TEXT NOT NULL, 
                Percentagem_ICMS20 TEXT NOT NULL, 
                Valor_ICMS20 TEXT NOT NULL,
                CST_ICMS30 TEXT NOT NULL,
                CST_ICMS40 TEXT NOT NULL,
                CST_ICMS41 TEXT NOT NULL,
                CST_ICMS50 TEXT NOT NULL,
                CST_ICMS51 TEXT NOT NULL,
                CST_ICMS60 TEXT NOT NULL,
                CST_ICMS70 TEXT NOT NULL,
                CST_ICMS90 TEXT NOT NULL, 
                    
                
                
                PRIMARY KEY(Idtabela)
                );                            
              
                """)    
        
        
    def tabela_saida(self):
        
        self._host='clientes1304.mysql.uhserver.com'
        self._user='samuel1304'
        self._passwd='@lb130488'
        self._database='tabelaclientes'
        self.con = None        
        
        self.con = mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._passwd,
            database=self._database
           )
     
        cursor = self.con.cursor()
        
        sql = ("SELECT NOMEDAEMPRESA, FANTASIA, dataatividade, CAPITAL, opcao,ENDERECO, COMPLEMENTO, CIDADE, CEP, SOCIO, CNAE FROM Tabela_Clientes")
        cursor.execute(sql)
        
        
        for i in cursor:
            self.campo = QTreeWidgetItem(self.tabela_geral_2, i)
       
        

                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window= Login()
    window.show()
    app.exec_()
    
            