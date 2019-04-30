import psycopg2
from psycopg2.extras import RealDictCursor
from config.configDB import ConfigDB
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
import ast

class Dao:
    def __init__(self):
        db_string = 'postgresql+psycopg2://'+ConfigDB.user+':'+ConfigDB.password+'@'+ConfigDB.host+'/'+ConfigDB.dbname 
        self.connect_str = 'dbname='+ConfigDB.dbname+' user='+ConfigDB.user+' host='+ConfigDB.host+' password='+ConfigDB.password
        self.conn = psycopg2.connect(self.connect_str)
        #
        #register_default_json: (Create and register json typecasters). Para leituras de atributos json 
        # feitas pelo psycopg2, sera criado e registrado funcoes de conversao para estes atributos
        
        #ast.literal_eval: Converte a representacao em string de um dict() para um objeto dict()
        #
        psycopg2.extras.register_default_json(loads=lambda x: ast.literal_eval(x))
        Session = sessionmaker(create_engine(db_string)) 
        self.session = Session()

    def abrir(self,method):   
        if method == 'GET':
            #
            #cursor_factory: Parametro passado para definir um padrao para um cursor.

            #RealDictCursor: Define para um cursor um tipo base de retorno(rows),
            # rows que sao definidas de cursor.fetchall() 
            #
            cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            return (cursor)
        else:
            cursor = self.conn.cursor()
            return (cursor)
            
    def fechar(self):  
        self.conn.commit()
        self.conn.close()