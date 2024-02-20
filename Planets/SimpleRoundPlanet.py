from typing import List

from nptyping import NDArray, Shape, Float
from IObject import IObject
from Objects.IPlanet import IPlanet
from pyatmos import coesa76


class SimpleRoundPlanet(IPlanetWithAtmosphere):
    """Class defining simple round planet witch atmosphere"""

    def __init__(self,
                 mass: List[float],
                 originCoordinates: List[IObject.VectorIn3D],
                 rotationMatrix: List[NDArray[Shape["3,3"], Float]],
                 velocityMatrix: List[IObject.VectorIn3D],
                 accelerationMatrix: List[IObject.VectorIn3D],
                 momentOfInertiaMatrix: List[IObject.VectorIn3D],
                 angularVelocity: List[IObject.VectorIn3D],
                 angularAcceleration: List[IObject.VectorIn3D],
                 radius: float
                 ) -> None:
        super().__init__(mass,
                         originCoordinates,
                         rotationMatrix,
                         velocityMatrix,
                         accelerationMatrix,
                         momentOfInertiaMatrix,
                         angularVelocity,
                         angularAcceleration)
        self._radius = radius

    def getPlanetRadius(self, objectForRadius: IObject) -> float:
        return self._radius

    def getAirDensity(self, altitude: float) -> float:
        return float(coesa76(altitude/1e3).rho[0])




if __name__ == "__main__":
    for j in range(0, 10100, 100):
        print(str(j) + "m:", coesa76(j / 1e3).rho[0])

    print("----------------------------------------------")

    for j in range(0, 30100, 100):
        print(str(j) + "km:", coesa76(j).rho[0])