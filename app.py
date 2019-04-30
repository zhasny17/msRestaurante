import sys
from flask_sqlalchemy import SQLAlchemy
from config.configDB import ConfigDB
from doc.tratamentoErros import TratamentoErros
from config.flaskConfig import flask
from config.cacheConfig import cache
#
from resource.usuarioResource import UsuarioResouce
from resource.receitaResource import ReceitaResouce

aplicacao = sys.argv[0] #app.py
argumentos_passados = sys.argv[1:] #buscando os parametros repassados na execucao do app.py no terminal
print ('Executando a aplicacao: ' + str(aplicacao))
print ("E os argumentos passados sao: " + str(argumentos_passados))

configDB=ConfigDB(argumentos_passados) #instanciando um objeto da classe ConfigDB que recebe os argumentos passados pelo terminal

TratamentoErros().tratamentos(flask)
UsuarioResouce().chamaRota(flask,cache)
ReceitaResouce().chamaRota(flask,cache)   


if __name__ == '__main__':
    flask.run(host='0.0.0.0', port=configDB.port, debug=True)