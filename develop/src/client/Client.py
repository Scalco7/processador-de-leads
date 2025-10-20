from abc import ABC, abstractmethod

class Client(ABC):
    @abstractmethod
    def getSuggestion(self):
        pass