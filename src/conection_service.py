import requests as req

class Conection: 
    
    BASE_URL = "https://intregracao-site.presbiterio.org.br/api-ebd/"

    def getParams(self):
        base_uri = "parametros"
        return req.get(Conection.BASE_URL + base_uri)

    def getInfoFromCpf(self, cpf):
        base_uri = "consultacpf/"
        return req.get(Conection.BASE_URL + base_uri + cpf)
    
    def sendContribuition(self, data):
        base_uri = "cadastro-contribuicao"
        return req.post(Conection.BASE_URL + base_uri, data=data)