from Entidades.Pessoa.Pessoa import Pessoa
from Entidades.Pessoa.Cliente.Endereco import Endereco


class Cliente(Pessoa):

    def __init__(self, nome: str, cpf: str, telefone: str, endereco: Endereco):
        super().__init__(nome, cpf, telefone)
        self.__quantidade_pedidos = 0
        self.__endereco = endereco

    @property
    def quantidade_pedidos(self):
        return self.__quantidade_pedidos
    
    @quantidade_pedidos.setter
    def quantidade_pedidos(self, quantidade_pedidos):
        self.__quantidade_pedidos = quantidade_pedidos

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
