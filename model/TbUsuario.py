from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.configDB import ConfigDB
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from .base import Base


class TbUsuario(Base):
    __tablename__   = 'cdusuario'
    id              = Column(Integer, primary_key=True)
    nome            = Column("nome", String)
    email           = Column("email", String)   
    senha           = Column("senha", String) 
    qualificacao    = Column("qualificacao", String)                      
    tipo            = Column("tipo", String)   
        
    def __init__(self, obj):
        self.__dict__.update(obj)