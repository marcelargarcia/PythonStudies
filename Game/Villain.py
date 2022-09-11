from Character import *
class Villain(Character): #Herança
    def __init__(self, name):
        super(Villain, self).__init__(name)
        self.mapMoves()

    def mapMoves(self): #Polimorfismo
        super(Villain, self).mapMoves()
        self.mapMoves["StandingDD"] = "BackFlip"
    pass