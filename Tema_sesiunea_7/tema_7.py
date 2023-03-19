# import abc
from abc import abstractmethod, ABC
# from math import pi


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('cel mai probabil am colturi')


FormaGeometrica.descrie(FormaGeometrica)


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        self.aria = self.latura * self.latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):

        print(f'Getter: Latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter: Latura este {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters latura')
        self.__latura = None


patrat2 = Patrat(4)
patrat2.latura = 3
patrat2.latura
del patrat2.latura
patrat2.latura


class Cerc(FormaGeometrica):

    def init(self, raza):
        self.raza = raza

    def aria(self):
        self.aria = self.PI*(self.raza*self.raza)

    @property
    def raza(self):
        return self.raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Setter: Raza este {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Deleter: Am sters raza')
        self.__raza = None


cerc2 = Cerc()
cerc2.raza = 5
cerc2.raza
del cerc2.raza
cerc2.raza


def descrie():
    print("Eu nu am colturi")


descrie()

# nu am inteles la Polimorfism ce trebuie sa fac

# class Patrat(FormaGeometrica):
#     def centimetri(self):
#         print(input()"")
# obj_patrat = Patrat

# c():
#     def lungime(self):
#         lungime = (int(input("Introduce lungimea: ")))
#         latime = (int(input("Introduce lungimea: ")))
# class Cerc():
#     def raza_mica(self):
#         print("Baza mare")

# obj_patrat = Patrat(4)
# obj_cerc = Cerc()
# for descriere in (obj_patrat, obj_cerc):
#     descriere.aria()


