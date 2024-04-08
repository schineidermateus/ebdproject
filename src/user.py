from conection_service import Conection

class User():

    def getUserParams(self, cpf):
        conn = Conection()
        response = conn.getInfoFromCpf(cpf=cpf)

        if(response.status_code == 200):
            return response.json()