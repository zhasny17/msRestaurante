from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.configDB import ConfigDB
from sqlalchemy import Column, Integer, String, Date,ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime, date
from .base import Base

class TbIngrediente(Base):
    __tablename__       = 'cdingrediente'
    id                  = Column(Integer, primary_key=True)
    nome                = Column('nome', String)
    quantidade          = Column('quantidade', String)
    id_receita          = Column(Integer, ForeignKey('cdreceita.id' , onupdate="cascade"),nullable=False)
             

    def __init__(self, obj):
        if 'id' in obj:
            self.id             = obj['id']
        self.nome               = obj['nome']
        self.quantidade         = obj['quantidade']
        self.id_receita         = obj['id_receita']
