from abc import abstractmethod

from Objects.IPlanet import IPlanet


class IPlanetWithAtmosphere(IPlanet):

    @abstractmethod
    def getAirDensity(self, altitude: float) -> float:
        pass
