from Character import *
class Heroine(Character): #Herança
    def __init__(self, name, heroesGroup):
        super(Heroine, self).__init__(name)
        self.heroesGroup = heroesGroup
        self.mapMoves()

    def mapMoves(self): #Polimorfismo
        super(Heroine, self).mapMoves()
        self.mapMoves["StandingU"] = "Fly"
        self.mapMoves["FlyD"] = "Standing"
    pass
