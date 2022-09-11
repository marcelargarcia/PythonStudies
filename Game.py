class Character:
    def __init__(self, name):
        self.name = name

    def move(self, inicialState, action):
        Key = inicialState + action
        if self.mapMoves.get(Key, 'Not Found') == 'Not Found':
            return None
        return self.mapMoves.get(Key)

    def mapMoves(self):
        self.mapMoves = {}
        self.mapMoves["StandingB"] = "Jumping"
        self.mapMoves["StandingD"] = "Ducking"
        self.mapMoves["JumpingD"] = "Diving"
        self.mapMoves["DuckingU"] = "Standing"


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


class Villain(Character): #Herança
    def __init__(self, name):
        super(Villain, self).__init__(name)
        self.mapMoves()

    def mapMoves(self): #Polimorfismo
        super(Villain, self).mapMoves()
        self.mapMoves["StandingDD"] = "BackFlip"

    pass


if __name__ == '__main__':
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
