from util.utilitarios import Utilitarios

class ConfigDB:
    dbname = 'restaurante'
    user = 'postgres'
    host = 'localhost'
    password = 'ESTAGIO'
    port= '1401'

    def __init__(self, argumentos):
        utilitarios = Utilitarios()
        
        # recebendo os atributos pelo terminal
        __port = utilitarios.RetornaParametro(argumentos, '--port')
        __dbName = utilitarios.RetornaParametro(argumentos, '--dbName')
        __user = utilitarios.RetornaParametro(argumentos, '--user')
        __host = utilitarios.RetornaParametro(argumentos, '--host')
        __password = utilitarios.RetornaParametro(argumentos, '--password')
        # 

        if __port!='': self.port = int(__port)
        if __dbName!='': self.dbname = __dbName
        if __user!='': self.user = __user
        if __host!='': self.host = __host
        if __password!='': self.password = __password
        
        
        print('Configuration --------------->')
        print('Porta: ', self.port)
        print('dbname: ', self.dbname)
        print('user: ', self.user)
        print('host: ', self.host)
        print('password: ', self.password)
        print('----------------------------->')