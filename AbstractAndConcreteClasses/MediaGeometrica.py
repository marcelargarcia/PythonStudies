from Media import *

class MediaGeometrica(Media):
    def calcula(self):
        from math import prod
        return prod(self.numeros) ** (1/len(self.numeros))

#testeee