from typing import List
from IObject import IObject
from nptyping import NDArray, Shape, Float

from force_generarors.IAerodynamicForces import IAerodynamicForces
from force_generarors.IAerodynamicSurface import IAerodynamicSurface
from force_generarors.IEngine import IEngine
from force_generarors.IThruster import IThruster


class IRocket(IObject):
    def __init__(self,
                 mass: List[float],
                 originCoordinates: List[IObject.VectorIn3D],
                 rotationMatrix: List[NDArray[Shape["3,3"], Float]],
                 velocityMatrix: List[IObject.VectorIn3D],
                 accelerationMatrix: List[IObject.VectorIn3D],
                 momentOfInertiaMatrix: List[IObject.VectorIn3D],
                 angularVelocity: List[IObject.VectorIn3D],
                 angularAcceleration: List[IObject.VectorIn3D],
                 ) -> None:
        super().__init__(mass,
                         originCoordinates,
                         rotationMatrix,
                         velocityMatrix,
                         accelerationMatrix,
                         momentOfInertiaMatrix,
                         angularVelocity,
                         angularAcceleration)
        self.engines: List[IEngine] = []
        self.aerodynamicSurfaces: List[IAerodynamicSurface] = []
        self.thrusters: List[IThruster] = []
        self.aerodynamicForces: List[IAerodynamicForces] = []

    def addEngines(self, *engines: IEngine) -> None:
        for engine in engines:
            self.engines.append(engine)

    def addAerodynamicSurfaces(self, *aerodynamicSurfaces: IAerodynamicSurface) -> None:
        for aerodynamicSurface in aerodynamicSurfaces:
            self.aerodynamicSurfaces.append(aerodynamicSurface)

    def addThruster(self, *thrusters: IThruster) -> None:
        for thruster in thrusters:
            self.thrusters.append(thruster)

