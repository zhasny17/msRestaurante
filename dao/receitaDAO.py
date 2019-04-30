from .dao import Dao
import json
from flask import Flask, jsonify
from datetime import datetime, date
from doc.tratamentoErros import emptyResponse
from util.jsonEncoder import json_encoder
from model.TbReceita import TbReceita

session = Dao().session

class ReceitaDAO:

    def __init__(self):   
        self.dao = Dao()

    def getAll(self, parametros):
        sql = session.query(TbReceita).all()
        return json.loads(json.dumps(sql, cls=json_encoder(False, ['ingredientes'])))

    def getById(self,id): 
        sql = session.query(TbReceita).filter(TbReceita.id == id).first()
        return json.loads(json.dumps(sql, cls=json_encoder(False, ['ingredientes'])))

    def remove(self,id):
        obj = session.query(TbReceita).filter(TbReceita.id==id).first()
        if not obj:
            raise emptyResponse()
        else:
            try:
                session.delete(obj)
                session.commit()
            except:
                session.rollback()
                raise

    def update(self, obj):
        try:       
            tbObjeto = TbReceita(obj)
            session.merge(tbObjeto)
            session.commit()
            session.refresh(tbObjeto)
            obj = self.getById(obj['id'])
        except:
            session.rollback()
            raise
        return obj

    def insert(self, obj):
        try:
            tbObjeto = TbReceita(obj)
            session.add(tbObjeto)
            session.commit()
            session.refresh(tbObjeto)
            obj['id'] = tbObjeto.id
        except:
            session.rollback()
            raise
        return obj