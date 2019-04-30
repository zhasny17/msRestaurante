#!flask/bin/python
import json
from flask import jsonify, request
from sqlalchemy import Column, Integer, String, Date,JSON, ForeignKey
from doc.tratamentoErros import emptyResponse
from datetime import datetime, date, timedelta
from dao.receitaDAO import ReceitaDAO
from .usuarioRN import UsuarioRN

class ReceitaRN:

    def findAll(self, parametros):
        rows = ReceitaDAO().getAll(parametros)  
        return rows
    
    def findById(self, id):
        row = ReceitaDAO().getById(id)  
        return row
    
    def remove(self, id):
        return jsonify (ReceitaDAO().remove(id))

    def update(self, id, obj):
        obj = self.validarUpdate(id, obj)
        obj = ReceitaDAO().update(obj)
        return obj

    def validarUpdate(self, id, obj):
        objAtual = self.findById(id)
        if objAtual == None:
            raise  emptyResponse(message = 'Receita nao existe!') 
        #
        objNovo = self.atualizarAtributos(objAtual, obj)
        self.validarObjeto(objNovo)
        return objNovo

    def insert(self, obj):
        obj = self.validarInsert(obj)
        obj = ReceitaDAO().insert(obj)
        return obj

    def validarInsert(self, obj):
        obj = self.atualizarObjeto(obj)
        self.validarObjeto(obj)
        return obj

    def atualizarObjeto(self, obj):
        tbUsuario = UsuarioRN().findById(obj['idUsuario'])
        if tbUsuario!=None:
            obj['idUsuario'] = tbUsuario.get("id")
        return obj

    def validarObjeto(self, obj):
        if 'nome' not in obj:
            raise  emptyResponse(message = 'Nome de uma receita e campo obrigatorio') 
        if 'idUsuario' not in obj:
            raise  emptyResponse(message = 'Receita tem que pertencer a um usuario') 

    def atualizarAtributos(self, objAtual, obj):
        for atributo in obj:
            objAtual[atributo] = obj[atributo]
        return objAtual



