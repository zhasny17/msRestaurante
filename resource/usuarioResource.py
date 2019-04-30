from flask import jsonify, request
from doc.tratamentoErros import emptyResponse
from rn.usuarioRN import UsuarioRN
import json

class UsuarioResouce:
    def chamaRota(self,flask,cache):

        def make_cache_key(*args, **kwargs):
            path = request.path
            data = request.data.decode('latin1')
            args = str(hash(frozenset(request.args.items())))
            return (path + args + data).encode('utf-8')

        @flask.route('/usuario', methods=['GET'])
        @cache.cached(timeout=5)
        def getAllUsuarios():
            parametros = dict()
            #####################################
            # nenhum parametro ainda eh passado # 
            #####################################
            rows = UsuarioRN().findAll(parametros)
            return response(rows)

        @flask.route('/usuario/<string:id>', methods=['GET'])
        @cache.cached(timeout=5)
        def getUsuarioById(id):
            row = UsuarioRN().findById(id)
            return response(row)
       
        @flask.route('/usuario/<id>', methods=['DELETE'])
        def deleteUsuario(id):
            UsuarioRN().remove(id)
            return "Usuario foi removida"

        @flask.route('/usuario/<id>',methods=['PUT'])
        @cache.cached(timeout=5, key_prefix=make_cache_key)
        def putUsuario(id):
            if not request.data:
                raise emptyResponse(message='Dados necessarios nao fornecidos!')
            else:
                obj = json.loads(request.data)
                row = UsuarioRN().update(id, obj) 
                return response(row)

        @flask.route('/usuario',methods=['POST'])
        @cache.cached(timeout=5, key_prefix=make_cache_key)
        def postUsuario(): 
            obj = json.loads(request.data)
            return response(UsuarioRN().insert(obj))
        
        def response(obj):
            if not obj:
                raise emptyResponse()
            else:
                return jsonify(obj) 
