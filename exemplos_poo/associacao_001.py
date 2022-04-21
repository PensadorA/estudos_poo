
class Cachorro:

    @staticmethod
    def latir():
        print('au au au')

    @staticmethod
    def abanar_rabo():
        print('abanando rabo')


class Pessoa:

    @staticmethod
    def afagar_animal(animal):
        animal.abanar_rabo()


ana = Pessoa()
rex = Cachorro()
ana.afagar_animal(rex)
