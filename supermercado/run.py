from carrinho import *


class Supermercado:

    @staticmethod
    def menu():
        print('Abrindo terminal de vendas')
        Supermercado.terminal()

    @staticmethod
    def terminal():
        print('Bem vindo')
        print('aperte ! no nome para finalizar ')
        compras = Carrinho()
        while True:
            nome = str(input('Digite o nome do produto'))
            if nome == '!':
                break
            preco = None
            while True:
                try:
                    preco = float(input('Digite o preco do produto, padrão americano de ponto'))
                    break
                except:
                    print('Você digitou um preço inválido, tente novamente.')

            compras.passar_produto(nome, preco)
        dinheiro = None
        while True:
            try:
                dinheiro = float(input('Digite o pagamento, padrão americano de ponto'))
                break
            except:
                print('Você digitou um valor inválido, tente novamente.')

        compras.pagar(dinheiro)


if __name__ == '__main__':
    Supermercado.menu()

