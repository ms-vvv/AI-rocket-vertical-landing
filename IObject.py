from abc import ABC, abstractmethod
from typing import List

import numpy as np
from nptyping import NDArray, Shape, Float


class IObject(ABC):
    """Interface defining basic physical object"""

    VectorIn3D = NDArray[Shape["3"], Float]

    numberOfObjects: int = 0

    def __init__(self,
                 initialMass: float,
                 originCoordinates: VectorIn3D,
                 rotationMatrix: NDArray[Shape["3,3"], Float],
                 velocityMatrix: VectorIn3D,
                 accelerationMatrix: VectorIn3D,
                 momentOfInertiaMatrix: VectorIn3D,
                 angularVelocity: VectorIn3D,
                 angularAcceleration: VectorIn3D
                 ) -> None:
        IObject.numberOfObjects += 1
        self.mass: List[float] = [initialMass]  # Mass of the object
        self._originCoordinates: List[IObject.VectorIn3D] = [originCoordinates]  # Position of origin of coordinate system defining object
        self._rotationMatrix: List[NDArray[Shape["3,3"], Float]] = [rotationMatrix]  # Rotation matrix composed of vectors defining local coordinate system
        self._velocityMatrix: List[IObject.VectorIn3D] = [velocityMatrix]  # [X, Y, Z] components of velocity in local coordinate system
        self._accelerationMatrix: List[IObject.VectorIn3D] = [accelerationMatrix]  # [X, Y, Z] components of acceleration in local coordinate system
        self._momentOfInertiaMatrix: List[IObject.VectorIn3D] = [momentOfInertiaMatrix]  # [X, Y, Z] components of moment of inertia around object axis of local coordinate system
        self._angularVelocity: List[IObject.VectorIn3D] = [angularVelocity]  # [X, Y, Z] components of angular velocity of object axis of local coordinate system
        self._angularAcceleration: List[IObject.VectorIn3D] = [angularAcceleration]  # [X, Y, Z] components of angular acceleration of object axis of local coordinate system
        self.originCoordinatesOffset: IObject.VectorIn3D = np.zeros(3)
        self.angularVelocityOffset: IObject.VectorIn3D = np.zeros(3)
        self.velocityOffset: IObject.VectorIn3D = np.zeros(3)
        self.rotationMatrixOffset: NDArray[Shape["3,3"], Float] = np.zeros((3, 3))

    @property
    def currentOriginCoordinates(self) -> VectorIn3D:
        return self._originCoordinates[-1] + self.originCoordinatesOffset

    @property
    def currentVelocity(self) -> VectorIn3D:
        return self._velocityMatrix[-1] + self.velocityOffset

    @property
    def currentRotationMatrix(self) -> NDArray[Shape["3,3"], Float]:
        return self._rotationMatrix[-1] + self.rotationMatrixOffset

    @property
    def currentAngularVelocity(self) -> VectorIn3D:
        return self._angularVelocity[-1] + self.angularVelocityOffset

    def updateAccelerationVector(self, newAccelerationVector: VectorIn3D) -> None:
        self._accelerationMatrix.append(newAccelerationVector)

    def updateVelocityVector(self, newVelocityVector: VectorIn3D) -> None:
        self._velocityMatrix.append(newVelocityVector)

    def updatePositionVector(self, newPositionVector: VectorIn3D) -> None:
        self._originCoordinates.append(newPositionVector)

    def updateAngularAccelerationVector(self, newAngularAccelerationVector: VectorIn3D) -> None:
        self._angularAcceleration.append(newAngularAccelerationVector)

    def updateAngularVelocityVector(self, newAngularVelocityVector: VectorIn3D) -> None:
        self._angularVelocity.append(newAngularVelocityVector)

    def updateRotationMatrix(self, newRotationMatrix: NDArray[Shape["3,3"], Float]) -> None:
        self._rotationMatrix.append(newRotationMatrix)

