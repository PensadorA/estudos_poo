from datetime import date

lista_pessoas = []


class Pessoa:
    id = 1000

    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__data_cadastro = date.today()
        self.__id = Pessoa.id
        Pessoa.id += 1

    def nome(self):
        return self.__nome

    def idade(self):
        return self.__idade

    def cpf(self):
        return self.__cpf

    def data_cadastor(self):
        return self.__data_cadastro

    def selec_id(self):
        return self.__id

    def __del__(self):
        print('Pessoa deletada com sucesso.')


def cadastra():
    global lista_pessoas
    nome = input('Digite o nome da pessoa ')
    idade = input('Digite a idade da pessoa ')
    cpf = input('Digite o cpf da pessoa ')
    lista_pessoas.append(Pessoa(nome, idade, cpf))
    print('Pessoa Cadastra com sucesso ')
    menu()


def selecione_pessoa():
    global lista_pessoas
    idpessoa = int(input('Digite o id da pessoa'))
    for i in lista_pessoas:
        if idpessoa == i.selec_id():
            print('Pessoa encontrada')
            print(i.nome())
            print(i.idade())
            print(i.cpf())
    menu()


def exluir():
    global lista_pessoas

    idpessoa = int(input('Digite o id da pessoa'))
    for i in lista_pessoas:
        if idpessoa == i.selec_id():
            del i
    menu()


def todos():
    global lista_pessoas
    for i in lista_pessoas:
        print('_________________')
        print(i.nome())
        print(i.idade())
        print(i.cpf())
        print('_________________')
    menu()


def menu():
    print('1 para cadastrar')
    print('2 para escolher uma pessoa')
    print('3 excluir pessoa')
    print('4  ver todos')
    value = int(input('Digite uma opção '))
    if value == 1:
        cadastra()

    elif value == 2:
        selecione_pessoa()

    elif value == 3:
        exluir()

    elif value == 4:
        todos()

    else:
        menu()


if __name__ == '__main__':
    menu()
