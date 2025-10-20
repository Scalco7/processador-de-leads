from abc import ABC, abstractmethod

class Client(ABC):
    @abstractmethod
    def get_suggestion(self):
        pass