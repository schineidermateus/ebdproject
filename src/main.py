from user import User
from conection_service import Conection

def main():
    user = User()
    
    userInfo = user.getUserParams(cpf="16308006785")
    
    ebdInfos = getEbdInfos()
    
    if ebdInfos is None or userInfo is None:
        return
    
    # Users
    nome = userInfo['nome']
    pastor = userInfo['pastor']
    igreja = userInfo['igreja']
    cidade = userInfo['cidade']
    uf = userInfo['uf']
    email = userInfo['email']
    celular = userInfo['celular']

    # EBDs
    ebdId = ebdInfos['id']
    ebdTitulo = ebdInfos['titulo']
    ebdData = ebdInfos['data']

    print(ebdInfos, userInfo)



def getEbdInfos():
    con = Conection()
    params = con.getParams()

    if params.status_code == 200:
        return params.json()["ebds"][0]

if __name__ == "__main__":
    main()
