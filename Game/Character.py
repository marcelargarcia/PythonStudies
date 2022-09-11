from abc import ABC, abstractmethod
class Character(ABC):
    def __init__(self, name):
        self.name = name
        self.mapMoves = {}
        #self.mappingMoves()

    def move(self, inicialState, action):
        Key = inicialState + action
        if self.mapMoves.get(Key, 'Not Found') == 'Not Found':
            return None
        return self.mapMoves.get(Key)

    @abstractmethod
    def mappingMoves(self):
        self.mapMoves["StandingB"] = "Jumping"
        self.mapMoves["StandingD"] = "Ducking"
        self.mapMoves["JumpingD"] = "Diving"
        self.mapMoves["DuckingU"] = "Standing"

