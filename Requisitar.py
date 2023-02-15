import pip._vendor.requests

class Requisitar:
    def __init__(self, cep):
        self.cep = cep
        self.link = f'https://viacep.com.br/ws/{self.cep}/json/'
        self.response = self.request()

    
    def request(self):
        response = pip._vendor.requests.get(self.link)
        dic_response = response.json()
        self.estado = dic_response['uf']
        self.cidade = dic_response['localidade']
        self.rua = dic_response['logradouro']
        self.bairro = dic_response['bairro']
        self.endereco = (self.estado, self.cidade, self.rua, self.bairro)
<<<<<<< HEAD
        return None
=======
        return None
>>>>>>> 7bc3c1321a6e2acd6c6287c1f8c080300a1292b0
