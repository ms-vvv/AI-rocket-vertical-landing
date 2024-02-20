from typing import List

import numpy as np
from nptyping import NDArray, Shape, Float

from IObject import IObject
from Objects.IRocket import IRocket


class SimpleCylindricalRocket(IRocket):
    def __init__(self,
                 mass: float,
                 originCoordinates: IObject.VectorIn3D,
                 rotationMatrix: NDArray[Shape["3,3"], Float],
                 velocityMatrix: IObject.VectorIn3D,
                 accelerationMatrix: IObject.VectorIn3D,
                 angularVelocity: IObject.VectorIn3D,
                 angularAcceleration: IObject.VectorIn3D,
                 positionOfReferencePoint: IObject.VectorIn3D,
                 rocketRadius: float,
                 rocketLength: float
                 ) -> None:
        super().__init__([mass],
                         [originCoordinates],
                         [rotationMatrix],
                         [velocityMatrix],
                         [accelerationMatrix],
                         [self._calculateMomentOfInertia()],
                         [angularVelocity],
                         [angularAcceleration])
        self.rocketLength = rocketLength
        self.positionOfReferencePoint = positionOfReferencePoint
        self.rocketRadius = rocketRadius

    def _calculateMomentOfInertia(self) -> IObject.VectorIn3D:
        x_moment_of_inertia = self.mass[-1] * self.rocketRadius**2
        y_moment_of_inertia = (1/12) * self.mass[-1] * (6*self.rocketRadius**2 + 4*self.rocketLength**2)
        z_moment_of_inertia = y_moment_of_inertia

        return np.array([x_moment_of_inertia, y_moment_of_inertia, z_moment_of_inertia])
