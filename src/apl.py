from user import User
from conection_service import Conection
from formulario import Formulario

cpfs = []
formulario = Formulario()

CATEGORIAS = {
    'sugestao' : 1,
    'participacao' : 2,
    'duvidas' : 3,
    'experiencias' : 4	
}

def sendRequest():
    prepareCpfsList()

    ebdInfos = getEbdData()
    ebdId = ebdInfos['id']

    for cpf in cpfs:
        data = getJsonData(cpf=cpf, ebdId=ebdId)

        if data is None:
            continue

        print(data)

        # Nesse ponto eu faço a request

def getJsonData(cpf, ebdId):
    user = User()
    userInfo = user.getUserParams(cpf=cpf)

    if  userInfo is None:
        return

    contribuicao = '<p>' + formulario.getContribuicao() + '</p>'

    return {
        'aceite_termo' : True,
        'categoria_id' : CATEGORIAS['participacao'],
        'celular' : userInfo['celular'],
        'email' : userInfo['cidade'],
        'contribuicao' : contribuicao,
        'denominacao_id' : 21,
        'denominacao_outras' : '',
        'ebd_id' : ebdId,
        'email' : userInfo['email'],
        'funcao' : '',
        'funcao_id' : '',
        'nome' : userInfo['nome'],
        'trabalho_id' : "",
        'uf' : userInfo['uf']
    }


def getEbdData():  
    ebdInfos = getEbdInfos()
    
    if ebdInfos is None :
        return
    
    return ebdInfos
      

def getEbdInfos():
    con = Conection()
    params = con.getParams()

    if params.status_code == 200:
        return params.json()["ebds"][0]

def prepareCpfsList():
    cpfsList = formulario.getCpf().split(",")

    for cpf in cpfsList:
        cpf = cpf.replace(" ", "")
        cpf = cpf.replace("\n", "")
        cpf = cpf.replace("\r", "")
        cpf = cpf.replace(",", "")
        cpf = cpf.replace(";", "")
        cpf = cpf.replace(".", "")
        cpf = cpf.replace("-", "")
        if len(cpf) == 11:
            cpfs.append(cpf)

def mainController():
    janela = formulario.getJanela()
    janela.mainloop()