from item import *


class Carrinho:
    def __init__(self):
        self.__carrinho = []
        self.__total = 0

    def passar_produto(self, nome, preco):
        self.__carrinho.append(Item(nome, preco))
        self.__total += preco
        print(f'Produto {nome} foi adicionado com sucesso')
        print(self.__total)
        print('________________-')

    def _total(self):
        return f'Sua compra está no momento em {self.__total} R$'

    def pagar(self, valor):
        if valor >= self.__total:
            print(f'Você deve retornar ao cliente {valor - self.__total} R$')


    def __del__(self):
        print('Finalizado com sucesso')
