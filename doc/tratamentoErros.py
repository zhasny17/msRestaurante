# -*- coding: utf-8 -*-
from flask import jsonify

class TratamentoErros():
    def tratamentos(self,flask):

        @flask.errorhandler(400)
        def error_found(error):
            flask.logger.error('Erros internos causados pelo consumidor (client) do Microserviço, como erros de validação ou inconsistência de informações.')
            return 'Erros internos causados pelo consumidor (client) do Microserviço, como erros de validação ou inconsistência de informações.',400
            
        @flask.errorhandler(401)
        def denied_error(error):
            flask.logger.error('Não autorizado, é necessário autenticação!')
            return 'Não autorizado, é necessário autenticação!',401
            
        @flask.errorhandler(403)
        def permission_error(error):
            flask.logger.error('Proibido, é necessário permissão de acesso a função!')
            return 'Proibido, é necessário permissão de acesso a função!',403
            
        @flask.errorhandler(404)
        def not_found(error):
            flask.logger.error('Não encontrado, verifique se o caminho foi informado corretamente ou se existe!')
            return 'Não encontrado, verifique se o caminho foi informado corretamente ou se existe!',404

            
        @flask.errorhandler(500)
        def server_error(error):
            flask.logger.error('Erros internos causados pelo servidor, tente novamente em alguns instantes, se o erro persistir contate a equipe de suporte da HR!')
            return 'Erros internos causados pelo servidor, tente novamente em alguns instantes, se o erro persistir contate a equipe de suporte da HR!',500

        @flask.errorhandler(emptyResponse)
        def handle_invalid_usage(error):
            response = error.get_message()
            return response,404

class emptyResponse(Exception):
    def __init__(self,message=None):
        Exception.__init__(self)
        if message == None:
            self.message = 'O recurso nao foi encontrado!'
        else:
            self.message = message

    def get_message(self):
        return self.message