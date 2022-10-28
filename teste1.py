from cgitb import reset
import os
import numpy as np
import sqlite3
import xml.etree.ElementTree as Et
from datetime import date
import pandas as pd


class Read_xml():
    def __init__(self, directory) -> None:
        self.directory = directory
        
    def all_files(self):
        return [os.path.join(self.directory, arq) for arq in os.listdir(self.directory) 
                if arq.lower().endswith(".xml")]
        
    def nfe_data(self,xml):
        root = Et.parse(xml).getroot()
        nsNFe = {"ns":"http://www.portalfiscal.inf.br/nfe"}
        
        #DADOS DA NFE
        
        serie = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:serie", nsNFe))
        nfe = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:nNF", nsNFe))
        data_emissao = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:dhEmi", nsNFe))
        data_emissao = F"{data_emissao[8:10]}/{data_emissao[5:7]}/{data_emissao[:4]}"
        cnpj_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:CNPJ", nsNFe))
        nome_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:xNome", nsNFe))
        logradouro_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:xLgr", nsNFe))
        numero_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:nro", nsNFe))
        complemento_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:xCpl", nsNFe))
        bairro_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:xBairro", nsNFe))
        codigo_municipio_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:cMun", nsNFe))
        Municipio_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:xMun", nsNFe))
        uf_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:UF", nsNFe))
        cep_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:CEP", nsNFe))
        cod_pais_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:cPais", nsNFe))
        pais_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:xPais", nsNFe))
        inscricao_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:IE", nsNFe))

        cnpj_destinatario = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:CNPJ", nsNFe))
        nome_destinatario = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:xNome", nsNFe))
        logradouro_destinatario = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:xLgr", nsNFe))
        numero_destinatario = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:nro", nsNFe))
        complemento_destinatario = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:xCpl", nsNFe))
        bairro_destinatario = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:xBairro", nsNFe))
        codigo_municipio_destinatario = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:cMun", nsNFe))
        Municipio_destinatario = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:xMun", nsNFe))
        uf_destinatario = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:UF", nsNFe))
        cep_destinatario = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:CEP", nsNFe))
        inscricao_destinatario = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:IE", nsNFe))
               
        chave_de_acesso = self.check_none(root.find("./ns:protNFe/ns:infProt/ns:chNFe", nsNFe))
        
        
        itemNota = 1
                
        notas = []
       
        
        for item in root.findall("./ns:NFe/ns:infNFe/ns:det", nsNFe):
           
        #DADOS DOS ITENS
            
            codigo_barras = self.check_none(item.find("./ns:prod/ns:cEAN", nsNFe))
            produto = self.check_none(item.find("./ns:prod/ns:xProd", nsNFe))
            NCM = self.check_none(item.find("./ns:prod/ns:NCM", nsNFe))
            CFOP = self.check_none(item.find("./ns:prod/ns:CFOP", nsNFe))
            unidade_comercial = self.check_none(item.find("./ns:prod/ns:uCom", nsNFe))
            quantidade_comercial = self.check_none(item.find("./ns:prod/ns:qCom", nsNFe))
            valor_unidade_comercial = self.check_none(item.find("./ns:prod/ns:vUnCom", nsNFe))
            valor_total_produto = self.check_none(item.find("./ns:prod/ns:vProd", nsNFe))
            quantidade_produto = self.check_none(item.find("./ns:prod/ns:qTrib", nsNFe))
            valor_produto = self.check_none(item.find("./ns:prod/ns:vUnTrib", nsNFe))
            
        #for id, xml in enumerate(item.findall("./ns:imposto", nsNFe)):
            #item.set ('id', str(id))
            #item.write("./ns:imposto", nsNFe)
        
            
            CST_ICMS00 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS00/ns:CST", nsNFe))
            cod_origem00 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS00/ns:orig", nsNFe))
            Base_ICMS00 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS00/ns:vBC", nsNFe))
            Percentagem_ICMS00 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS00/ns:pICMS", nsNFe))
            Valor_ICMS00 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS00/ns:vICMS", nsNFe))
            CST_ICMS10 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS10/ns:CST", nsNFe))
            cod_origem10 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS10/ns:orig", nsNFe))
            Base_ICMS10 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS10/ns:vBC", nsNFe))
            Percentagem_ICMS10 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS10/ns:pICMS", nsNFe))
            Valor_ICMS10 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS10/ns:vICMS", nsNFe))
            CST_ICMS20 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS20/ns:CST", nsNFe))
            cod_origem20 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS20/ns:orig", nsNFe))
            Base_ICMS20 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS20/ns:vBC", nsNFe))
            Percentagem_ICMS20 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS20/ns:pICMS", nsNFe))
            Valor_ICMS20 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS20/ns:vICMS", nsNFe))
            CST_ICMS30 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS30/ns:CST", nsNFe))
            CST_ICMS40 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS40/ns:CST", nsNFe))
            CST_ICMS41 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS41/ns:CST", nsNFe))
            CST_ICMS50 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS50/ns:CST", nsNFe))
            CST_ICMS51 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS51/ns:CST", nsNFe))
            CST_ICMS60 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS60/ns:CST", nsNFe))
            CST_ICMS70 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS70/ns:CST", nsNFe))
            
            cod_origem70 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS70/ns:orig", nsNFe))
            Base_ICMS70 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS70/ns:vBC", nsNFe))
            Percentagem_ICMS70 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS70/ns:pICMS", nsNFe))
            Valor_ICMS70 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS70/ns:vICMS", nsNFe))
            
            CST_ICMS90 = self.check_none(item.find("./ns:imposto/ns:ICMS/ns:ICMS90/ns:CST", nsNFe))
            
            CST_PIS = self.check_none(item.find("./ns:imposto/ns:PIS/ns:PISAliq/ns:CST", nsNFe))
            Base_PIS = self.check_none(item.find("./ns:imposto/ns:PIS/ns:PISAliq/ns:vBC", nsNFe))
            Percentagem_PIS = self.check_none(item.find("./ns:imposto/ns:PIS/ns:PISAliq/ns:pPIS", nsNFe))
            Valor_PIS = self.check_none(item.find("./ns:imposto/ns:PIS/ns:PISAliq/ns:vPIS", nsNFe))
            CST_COFINS = self.check_none(item.find("./ns:imposto/ns:COFINS/ns:COFINSAliq/ns:CST", nsNFe))
            Base_COFINS = self.check_none(item.find("./ns:imposto/ns:COFINS/ns:COFINSAliq/ns:vBC", nsNFe))
            Percentagem_COFINS = self.check_none(item.find("./ns:imposto/ns:COFINS/ns:COFINSAliq/ns:pCOFINS", nsNFe))
            Valor_COFINS = self.check_none(item.find("./ns:imposto/ns:COFINS/ns:COFINSAliq/ns:vCOFINS", nsNFe))
            
            
            #PIS = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:PIS", nsNFe))
            #CST_PIS = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:CST", nsNFe))
     
            dados = [nfe, serie, data_emissao, cnpj_emitente, nome_emitente, logradouro_emitente, 
            numero_emitente, complemento_emitente, bairro_emitente, codigo_municipio_emitente, 
            Municipio_emitente, uf_emitente, cep_emitente, cod_pais_emitente, pais_emitente, inscricao_emitente,  cnpj_destinatario, nome_destinatario, logradouro_destinatario, 
            numero_destinatario, complemento_destinatario, bairro_destinatario, codigo_municipio_destinatario, 
            Municipio_destinatario, uf_destinatario, cep_destinatario, inscricao_destinatario,  
            chave_de_acesso, codigo_barras, produto, NCM, CFOP, unidade_comercial, quantidade_comercial, 
            valor_unidade_comercial, valor_total_produto, quantidade_produto, valor_produto, 
            CST_ICMS00, cod_origem00, Base_ICMS00, Percentagem_ICMS00, Valor_ICMS00,CST_ICMS10,  
            cod_origem10, Base_ICMS10, Percentagem_ICMS10, Valor_ICMS10,CST_ICMS20,  cod_origem20,Base_ICMS20, Percentagem_ICMS20, Valor_ICMS20,
            CST_ICMS30, CST_ICMS40, CST_ICMS41, CST_ICMS50, CST_ICMS51,CST_ICMS60, CST_ICMS70, cod_origem70, Base_ICMS70, Percentagem_ICMS70, Valor_ICMS70, CST_ICMS90, CST_PIS, Base_PIS, Percentagem_PIS, Valor_PIS, CST_COFINS, Base_COFINS, Percentagem_COFINS, Valor_COFINS ]
            
            notas.append(dados)
            
            
            itemNota += 1
            
        return notas
        
      
                
    def check_none(self,var):
        if var == None:
            return ""
        else:
            try:
                return var.text.replace('.',',')
            except: 
                return var.text
     
     #def format_cnpj(self, cnpj):
         #try:
             #cnpj = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
            # return cnpj
         
         #except:
             #return ""
class Database():
    def __init__(self, name = "system.db") -> None:
        self.name = name
    
    def conecta(self):
        self.connection = sqlite3.connect(self.name)
  #  def consultar_tabela(self):
         
       # for x in myresult: 
      #  print(myresult) 
        
    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    def insert_data(self, full_dataset):
    
        cursor = self.connection.cursor()
       # cursor.execute("""SELECT * FROM sqlite_master WHERE type= 'table';""") 
       # myresult = cursor.fetchall() 
        cnx = sqlite3.connect('system.db')
        result = pd.read_sql_query("""SELECT * FROM sqlite_master WHERE type= 'table';""", cnx)
        novoresultado = pd.DataFrame(result['name'])
        
        res = novoresultado.values.tolist()
                     
        
        
            
        
        
        
        
      #  for x in myresult: 
        
      #  print(type(myresult))
      #  print(len(myresult))
       # novomyresult = (pd.DataFrame(myresult))
        
        
        campos_tabela = ('nfe', 'serie', 'data_emissao', 'cnpj_emitente', 'nome_emitente', 'logradouro_emitente', 
            'numero_emitente', 'complemento_emitente', 'bairro_emitente', 'codigo_municipio_emitente', 
            'Municipio_emitente', 'uf_emitente', 'cep_emitente', 'cod_pais_emitente', 'pais_emitente', 'inscricao_emitente', 'cnpj_destinatario','nome_destinatario', 'logradouro_destinatario', 
            'numero_destinatario', 'complemento_destinatario', 'bairro_destinatario', 'codigo_municipio_destinatario', 
            'Municipio_destinatario', 'uf_destinatario', 'cep_destinatario', 'inscricao_destinatario',
            'chave_de_acesso', 'codigo_barras', 'produto', 'NCM', 'CFOP', 'unidade_comercial', 'quantidade_comercial', 
            'valor_unidade_comercial', 'valor_total_produto', 'quantidade_produto', 'valor_produto',   
            'CST_ICMS00',  'cod_origem00','Base_ICMS00', 'Percentagem_ICMS00', 'Valor_ICMS00','CST_ICMS10',  
            'cod_origem10','Base_ICMS10', 'Percentagem_ICMS10', 'Valor_ICMS10','CST_ICMS20',  'cod_origem20','Base_ICMS20', 'Percentagem_ICMS20', 'Valor_ICMS20',
            'CST_ICMS30', 'CST_ICMS40', 'CST_ICMS41', 'CST_ICMS50', 'CST_ICMS51','CST_ICMS60', 'CST_ICMS70', 'cod_origem70', 'Base_ICMS70', 'Percentagem_ICMS70', 'Valor_ICMS70', 'CST_ICMS90', 'CST_PIS', 'Base_PIS', 'Percentagem_PIS', 'Valor_PIS', 'CST_COFINS', 'Base_COFINS', 'Percentagem_COFINS', 'Valor_COFINS')

   
                
        quantidade = "," .join (map(str, '?'*73))
        
       # query = f"""INSERT INTO Notas {campos_tabela} VALUES ({quantidade})"""
       # print('chegou mesmo')
        
       # query = f"""INSERT INTO Cliente24722646000140entrada {campos_tabela} VALUES ({quantidade})"""
       # cursor = self.connection.cursor()
       # sqliteConnection = sqlite3.connect('SQLite_Retrieving_system.db')
      #  cursor.execute("SELECT * FROM sqlite_master WHERE type='table'") 
  
       # myresult = cursor.fetchall()
       # print(cursor.fetchall())
        
        try:
            for nota in full_dataset:
               # myresult = 'Cliente24722646000140saida'
                Notas = str("Cliente")+ nota[3] + str("saida")
                novaNotas = str("Cliente")+ nota[16] + str("entrada")
                #Notas = str("Cliente")+ nota[3]
                for x in range(len(res)):
                    if Notas in res[x]:
                        print('chegou1+1')
                        query = f"""INSERT INTO {Notas} {campos_tabela} VALUES ({quantidade})"""
                        cursor.execute(query, tuple(nota))     
                        self.connection.commit()
                    elif novaNotas in res[x]:
                        query = f"""INSERT INTO {novaNotas} {campos_tabela} VALUES ({quantidade})"""
                        cursor.execute(query, tuple(nota))     
                        self.connection.commit()
                    else:
                        pass
                   
        except sqlite3.IntegrityError:
            print('nota ja existe no banco')
        
        
        
        
             
if __name__ == "__main__":
    db = Database()
    db.conecta()
    titulo = "Notas"
  #  db.consultar_tabela()
    print('conectado')
    xml = Read_xml("C:/Users/Usuário/OneDrive/SAMUEL/PROGRAMACAO/xml_teste/TESTECNPJ/")
    all = xml.all_files()
    
    for i in all:
        result = xml.nfe_data(i)
    db.close_connection()