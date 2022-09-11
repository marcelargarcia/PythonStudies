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
