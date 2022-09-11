from abc import ABC, abstractmethod


class Media(ABC):
    def __init__(self, numeros):
        self.numeros = numeros

    @abstractmethod
    def calcula(self):
        pass


# from Media import *
class MediaAritmetica(Media):
    def calcula(self):
        return sum(self.numeros) / len(self.numeros)


# from Media import *
class MediaGeometrica(Media):
    def calcula(self):
        from math import prod
        return prod(self.numeros) ** (1/len(self.numeros))


if __name__ == '__main__':
# from MediaAritmetica import *
# from MediaGeometrica import *
    L = [5,5,5]
    print(MediaAritmetica(L).calcula())
    print(MediaGeometrica(L).calcula())