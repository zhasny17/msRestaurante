class Utilitarios:

    def RetornaParametro(self, listaParametros, param ):
        retorno = ''
        for parametro in listaParametros:
            if parametro.find(param)>-1:
                vRetorno = parametro.split('=')
                if len(vRetorno)==2:
                    retorno = vRetorno[1]
        return retorno