from abc import abstractmethod
from abc import ABC


class IForceGenerator(ABC):

    @abstractmethod
    def getForce(self) -> float:
        pass
    
    @abstractmethod
    def getMoment(self) -> float:
        pass
    
