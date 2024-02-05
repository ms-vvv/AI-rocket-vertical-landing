from IObject import IObject
from nptyping import NDArray, Shape, Float
from abc import abstractmethod


class IPlanet(IObject):
    """Interface defining planet"""
    def __init__(self,
                 mass: float,
                 originCoordinates: IObject._VectorIn3D,
                 rotationMatrix: NDArray[Shape["3,3"], Float],
                 velocityMatrix: IObject._VectorIn3D,
                 accelerationMatrix: IObject._VectorIn3D,
                 momentOfInertiaMatrix: IObject._VectorIn3D,
                 angularVelocity: IObject._VectorIn3D,
                 angularAcceleration: IObject._VectorIn3D,
                 ) -> None:
        super().__init__(mass,
                         originCoordinates,
                         rotationMatrix,
                         velocityMatrix,
                         accelerationMatrix,
                         momentOfInertiaMatrix,
                         angularVelocity,
                         angularAcceleration)

    @abstractmethod
    def getPlanetRadius(self) -> float:
        pass


