from Heroine import *
from Villain import *

heroine = Heroine('Diana', 'Liga da Justiça')
villain = Villain('Lobo')
# print(type(heroine))
# print(type(villain))
# print(isinstance(heroine, Character))
# print(isinstance(villain, Character))

# Moves:
print(heroine.move("Standing", "U"))
print(villain.move("Standing", "U"))
print(heroine.mapMoves)
print(villain.mapMoves)
