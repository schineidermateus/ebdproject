import requests as req

class Conection: 
    
    BASE_URL = "https://intregracao-site.presbiterio.org.br/api-ebd/"

    def getParams():
        base_uri = "parametros"
        return req.get(Conection.BASE_URL + base_uri)

    def getInfoFromCpf(cpf):
        base_uri = "consultacpf/"
        return req.get(Conection.BASE_URL + base_uri + cpf)
    
    def sendContribuition(data):
        base_uri = "cadastro-contribuicao"
        return req.post(Conection.BASE_URL + base_uri, data=data)