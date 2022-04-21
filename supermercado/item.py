class Item:

    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    def promocao(self, desconto):
        self.__preco = self.__preco + (self.__preco * desconto)


a = Item('arroz', 10.00)
