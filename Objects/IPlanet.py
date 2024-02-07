from IObject import IObject
from abc import abstractmethod


class IPlanet(IObject):
    """Interface defining planet"""

    @abstractmethod
    def getPlanetRadius(self, objectForAltitude: IObject) -> float:
        pass


