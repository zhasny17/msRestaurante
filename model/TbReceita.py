from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.configDB import ConfigDB
from sqlalchemy import Column, Integer, String,Float, Date,JSON, ForeignKey
from sqlalchemy.orm import relationship, backref
from .base import Base
from .TbUsuario import TbUsuario
from .TbIngrediente import TbIngrediente
from datetime import datetime

class TbReceita(Base):
    __tablename__       = 'cdreceita'
    id                  = Column(Integer, primary_key=True)
    nome                = Column("nome", String)
    tipo_receita        = Column("tipo_receita", String)
    nota                = Column("nota", Float, default=0)                      
    id_usuario          = Column("id_usuario", Integer, ForeignKey('cdusuari.id'))
    ultimaatualizacao   = Column("ultimaatuali", Date, default= datetime.now()) 
    preparo             = Column("preparo", String)
    ingredientes        = relationship("TbIngrediente",cascade="all, delete-orphan" , passive_updates=True, uselist=True)
    

    def __init__(self, obj):
        if 'id' in obj:
            self.id             = obj['id']
        if 'idUsuario' in obj:
            self.id_usuario     = obj['idUsuario']               
        self.nome               = obj['nome']   
        self.tipo_receita       = obj['tipo_receita']                     
        self.nota               = obj['nota']   
        self.ultimaatualizacao  = obj['ultimaAtualizacao']   
        self.preparo            = obj['preparo']   
        

    