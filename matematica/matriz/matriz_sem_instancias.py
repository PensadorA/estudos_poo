
class Matriz:

    def soma_matriz(self, dados, dados1):
        if self._validar_soma(dados, dados1):
            acc = []
            acc_aux = []
            for a, b in zip(dados, dados1):
                for c, d in zip(a, b):
                    acc_aux.append(c+d)
                acc.append(acc_aux.copy())
                acc_aux.clear()
            return acc
        return 'Erro, as matrizes não podem ser somadas'

    def sub_matriz(self, dados, dados1):
        if self._validar_soma(dados, dados1):
            acc = []
            acc_aux = []
            for a, b in zip(dados, self.oposta(dados1)):
                for c, d in zip(a, b):
                    acc_aux.append(c+d)
                acc.append(acc_aux.copy())
                acc_aux.clear()
            return acc
        return 'Erro, as matrizes não podem ser subtraidas'


    @staticmethod
    def oposta(dados):
        acc = []
        acc_aux = []
        for a in dados:
            for b in a:
                acc_aux.append(b * -1)
            acc.append(acc_aux.copy())
            acc_aux.clear()
        return acc


    def _validar_soma(self, dados, dados1):
        for a, b in zip(dados, dados1):
            if len(a) != len(b):
                return False
        return True



f = [[1, 2, 3], [1, 2, 3], [1, 28, 3]]
g = [[2, 2, 3], [4, 2, 3], [5, 7, 3 ]]

h = Matriz().sub_matriz(f, g)
print(h)
