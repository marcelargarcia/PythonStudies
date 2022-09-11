from Quadrado import *
from Retangulo import *
from Engenheiro import *

engenheiro = Engenheiro('Marcela')
terreno1 = TerrenoQuadrado(2)
terreno2 = TerrenoRetangular(2,3)

engenheiro.medir_perimetro(terreno1)
engenheiro.medir_area(terreno1)