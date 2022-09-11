from typing import Type
from Formas import FormasInterface

class Engenheiro:
    def __init__(self, nome: str) -> None:
        self.nome = nome
    def medir_perimetro(self, terreno):
        perimetro = terreno.get_perimetro()
        print('{} mediu o perimetro: {} m'.format(self.nome, perimetro))

    def medir_area(self, terreno):
        area = terreno.get_area()
        print('{} mediu a area: {} m2'.format(self.nome, area))