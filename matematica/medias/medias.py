class Medias:
    @staticmethod
    def media_simples(dados):
        acc = 0
        for i in dados:
            acc += i
        return acc / len(dados)

    @staticmethod
    def media_ponderada(dados):
        acc_media = 0
        acc_pesos = 0
        for i in dados:
            acc_media += i * dados[i]
            acc_pesos += i
        return acc_media/acc_pesos

    @staticmethod
    def media_geometrica(dados):
        acc = 1
        for i in dados:
            acc *= i
        return acc ** (1/len(dados))

    @staticmethod
    def media_harmonica(dados):
        acc = 0
        for i in dados:
            acc += 1/i
        return len(dados)/acc


dados_simples = [1, 2, 3, 4, 5]
dados_ponderados = {7: 13, 25: 14, 5: 15, 2: 16}
dados_geometria = [8, 10, 40, 50]
dados_harmonica = [120, 80]

a = Medias.media_simples(dados_simples)
print(a)

b = Medias.media_ponderada(dados_ponderados)
print(b)

c = Medias.media_geometrica(dados_geometria)
print(c)

d = Medias.media_harmonica(dados_harmonica)
print(d)
