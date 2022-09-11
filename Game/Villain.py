from Character import *
class Villain(Character): #Herança
    def __init__(self, name):
        super(Villain, self).__init__(name)
        self.mappingMoves()

    def mappingMoves(self): #Polimorfismo
        super().mappingMoves()
        self.mapMoves["StandingDD"] = "BackFlip"
    pass