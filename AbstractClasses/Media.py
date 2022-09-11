from abc import ABC, abstractmethod

class Media(ABC):
    def __init__(self, numeros):
        self.numeros = numeros

    @abstractmethod
    def calcula(self):
        pass
