from abc import ABC, abstractmethod
from typing import List

import numpy as np
from nptyping import NDArray, Shape, Float


class IObject(ABC):
    """Interface defining basic physical object"""

    VectorIn3D = NDArray[Shape["3"], Float]

    numberOfObjects: int = 0

    def __init__(self,
                 mass: List[float],
                 originCoordinates: List[VectorIn3D],
                 rotationMatrix: List[NDArray[Shape["3,3"], Float]],
                 velocityMatrix: List[VectorIn3D],
                 accelerationMatrix: List[VectorIn3D],
                 momentOfInertiaMatrix: List[VectorIn3D],
                 angularVelocity: List[VectorIn3D],
                 angularAcceleration: List[VectorIn3D]
                 ) -> None:
        IObject.numberOfObjects += 1
        self.mass = mass  # Mass of the object
        self._originCoordinates = originCoordinates  # Position of origin of coordinate system defining object
        self._rotationMatrix = rotationMatrix  # Rotation matrix composed of vectors defining local coordinate system
        self._velocityMatrix = velocityMatrix  # [X, Y, Z] components of velocity in local coordinate system
        self._accelerationMatrix = accelerationMatrix  # [X, Y, Z] components of acceleration in local coordinate system
        self._momentOfInertiaMatrix = momentOfInertiaMatrix  # [X, Y, Z] components of moment of inertia around object axis of local coordinate system
        self._angularVelocity = angularVelocity  # [X, Y, Z] components of angular velocity of object axis of local coordinate system
        self._angularAcceleration = angularAcceleration  # [X, Y, Z] components of angular acceleration of object axis of local coordinate system
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
