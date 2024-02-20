from IObject import IObject
from abc import abstractmethod


class IPlanet(IObject):
    """Interface defining planet"""

    @abstractmethod
    def getPlanetRadius(self, objectForAltitude: IObject) -> float:
        pass

    def getAltitude(self, objectForAltitude: IObject) -> float:
        altitude: float = 0
        for i in range(3):
            altitude += (objectForAltitude.currentOriginCoordinates[i] - self.currentOriginCoordinates[i])**2

        altitude = altitude**0.5 - self.getPlanetRadius(objectForAltitude)

        return altitude

