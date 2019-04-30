#!flask/bin/python
import json
from flask import jsonify, request
from doc.tratamentoErros import emptyResponse
from dao.usuarioDAO import UsuarioDAO

class UsuarioRN:

    def findAll(self, parametros):
        return UsuarioDAO().getAll(parametros)
    
    def findById(self, id):
        return UsuarioDAO().getByCnpj(id)
    
    def findByEmail(self, email):
        return UsuarioDAO().getByEmail(email)
    
    def remove(self, id):
        return jsonify (UsuarioDAO().remove(id))

    def update(self, id, obj):
        obj = self.validarUpdate(id, obj)
        obj = UsuarioDAO().update(obj)
        return obj

    def validarUpdate(self, id, obj):
        objAtual = self.findById(id)
        if objAtual == None:
            raise  emptyResponse(message = 'Usuario nao cadastrado!') 
        #
        objNovo = self.atualizarAtributos(objAtual, obj)
        self.validarObjeto(objNovo)
        return objNovo

    def insert(self, obj):
        obj = self.validarInsert(obj)
        obj = UsuarioDAO().insert(obj)
        return obj

    def validarInsert(self, obj):
        self.validarObjeto(obj)
        # se o Email já estiver cadastrado
        objPsq = self.findByEmail(obj['email'])
        if objPsq != None:
            raise  emptyResponse(message = 'Usuario ja cadastrada: ' + objPsq['nome']) 
        return obj

    def validarObjeto(self, obj):
        if 'email' not in obj:
            raise  emptyResponse(message = 'Email e campo obrigatorio') 
        if 'nome' not in obj:
            raise  emptyResponse(message = 'Nome e campo obrigatorio') 

    def atualizarAtributos(self, objAtual, obj):
        for atributo in obj:
            objAtual[atributo] = obj[atributo]
        return objAtual

       