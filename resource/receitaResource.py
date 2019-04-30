# -*- coding: utf-8 -*-
from rn.receitaRN import ReceitaRN
from flask import jsonify, request
from datetime import datetime, date
from doc.tratamentoErros import emptyResponse
import json
import ast

class ReceitaResouce:
    def chamaRota(self,flask,cache):

        def make_cache_key(*args, **kwargs):
            path = request.path
            data = request.data.decode('latin1')
            args = str(hash(frozenset(request.args.items())))
            return (path + args + data)

        @flask.route('/receita', methods=['GET'])
        def getAllReceita():
            parametros = dict()
            #####################################
            # nenhum parametro ainda eh passado # 
            #####################################
            rows = ReceitaRN().findAll(parametros)
            return response(rows)

        @flask.route('/receita/<int:id>', methods=['GET'])
        @cache.cached(timeout=5)
        def getByIdReceita(id):
            return response(ReceitaRN().findById(id))
        
        @flask.route('/receita/<id>', methods=['DELETE'])
        def deleteReceita(id):
            ReceitaRN().remove(id)
            return "Item removido"

        @flask.route('/receita',methods=['POST'])
        #@cache.cached(timeout=5, key_prefix=make_cache_key)
        def postReceita(): 
            obj = json.loads(request.data)
            obj['dataHora'] = datetime.now()
            return response(ReceitaRN().insert(obj))

        @flask.route('/receita/<id>',methods=['PUT'])
        @cache.cached(timeout=5, key_prefix=make_cache_key)
        def putReceita(id):
            if not request.data:
                raise emptyResponse(message='Dados necessarios nao fornecidos!')
            else:
                obj = json.loads(request.data)
                row = ReceitaRN().update(id, obj)
                return response(row)

        def response(obj):
            if not obj:
                raise emptyResponse()
            else:
                print(obj)
                return jsonify(obj) 
