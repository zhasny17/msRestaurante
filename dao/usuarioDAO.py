from .dao import Dao
import json
from flask import Flask, jsonify
from doc.tratamentoErros import emptyResponse
from util.jsonEncoder import json_encoder
from model.TbUsuario import TbUsuario

session = Dao().session

class UsuarioDAO:

    def __init__(self):   
        self.dao = Dao()

    def getAll(self,parametros):
        sql = session.query(TbUsuario).all()
        return json.loads(json.dumps(sql, cls=json_encoder()))

    def getById(self,id): 
        sql = session.query(TbUsuario).filter(TbUsuario.id == id).first()
        return json.loads(json.dumps(sql, cls=json_encoder()))

    def getByEmail(self, email): 
        sql = session.query(TbUsuario).filter(TbUsuario.email == email).first()
        return json.loads(json.dumps(sql, cls=json_encoder()))

    def remove(self,id):
        obj = session.query(TbUsuario).filter(TbUsuario.id==id).first()
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
            tbObjeto = TbUsuario(obj)
            session.merge(tbObjeto)
            session.commit()

        except:
            session.rollback()
            raise
        return obj

    def insert(self, obj):
        try:
            tbObjeto = TbUsuario(obj)
            session.add(tbObjeto)
            session.commit()
            session.refresh(tbObjeto)
            obj['id'] = tbObjeto.id
        except:
            session.rollback()
            raise
        return obj



        

