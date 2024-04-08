from user import User
from conection_service import Conection

def main():
    user = User()
    
    userInfo = user.getUserParams(cpf="")
    
    ebdInfos = getEbdInfos()
    
    if ebdInfos is None:
        return

    print(ebdInfos, userInfo)


def getEbdInfos():
    con = Conection()
    params = con.getParams()

    if params.status_code == 200:
        return params.json()["ebds"][0]

if __name__ == "__main__":
    main()
