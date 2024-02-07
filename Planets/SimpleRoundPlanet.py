from nptyping import NDArray, Shape, Float
from IObject import IObject
from Objects.IPlanet import IPlanet
from pyatmos import coesa76


class SimpleRoundPlanet(IPlanet):
    """Class defining simple round planet witch atmosphere"""

    def __init__(self,
                 mass: float,
                 originCoordinates: IObject._VectorIn3D,
                 rotationMatrix: NDArray[Shape["3,3"], Float],
                 velocityMatrix: IObject._VectorIn3D,
                 accelerationMatrix: IObject._VectorIn3D,
                 momentOfInertiaMatrix: IObject._VectorIn3D,
                 angularVelocity: IObject._VectorIn3D,
                 angularAcceleration: IObject._VectorIn3D,
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

    def getAltitude(self, objectForAltitude: IObject) -> float:
        altitude: float = 0
        for object_coordinate in objectForAltitude.originCoordinates:
            altitude += (object_coordinate - self.originCoordinates[0])**2

        altitude = altitude**0.5 - self.getPlanetRadius(objectForAltitude)

        return altitude


if __name__ == "__main__":
    for i in range(0, 10100, 100):
        print(str(i) + "m:", coesa76(i / 1e3).rho[0])

    print("----------------------------------------------")

    for i in range(0, 30100, 100):
        print(str(i) + "km:", coesa76(i).rho[0])