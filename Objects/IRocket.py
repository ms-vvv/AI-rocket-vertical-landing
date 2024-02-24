from typing import List
from IObject import IObject
from nptyping import NDArray, Shape, Float

from force_generarors.IAerodynamicForces import IAerodynamicForces
from force_generarors.IAerodynamicSurface import IAerodynamicSurface
from force_generarors.IEngine import IEngine
from force_generarors.IForceGenerator import IForceGenerator
from force_generarors.IThruster import IThruster


class IRocket(IObject):
    def __init__(self,
                 initialMass: float,
                 originCoordinates: IObject.VectorIn3D,
                 rotationMatrix: NDArray[Shape["3,3"], Float],
                 velocityMatrix: IObject.VectorIn3D,
                 accelerationMatrix: IObject.VectorIn3D,
                 momentOfInertiaMatrix: IObject.VectorIn3D,
                 angularVelocity: IObject.VectorIn3D,
                 angularAcceleration: IObject.VectorIn3D,
                 referencePointLocation: IObject.VectorIn3D
                 ) -> None:
        super().__init__(initialMass,
                         originCoordinates,
                         rotationMatrix,
                         velocityMatrix,
                         accelerationMatrix,
                         momentOfInertiaMatrix,
                         angularVelocity,
                         angularAcceleration)
        self.forceGeneratingComponents: List[IForceGenerator] = []
        self.referencePointLocation: IObject.VectorIn3D = referencePointLocation

    def addForceGeneratingComponent(self, *forceGeneratingComponents: IForceGenerator) -> None:
        for component in forceGeneratingComponents:
            self.forceGeneratingComponents.append(component)
