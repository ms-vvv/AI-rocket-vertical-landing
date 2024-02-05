from abc import ABC
from nptyping import NDArray, Shape, Float



class IObject(ABC):
    """Interface defining basic physical object"""

    _VectorIn3D = NDArray[Shape["3"], Float]

    numberOfObjects: int = 0

    def __init__(self,
                 mass: float,
                 originCoordinates: _VectorIn3D,
                 rotationMatrix: NDArray[Shape["3,3"], Float],
                 velocityMatrix: _VectorIn3D,
                 accelerationMatrix: _VectorIn3D,
                 momentOfInertiaMatrix: _VectorIn3D,
                 angularVelocity: _VectorIn3D,
                 angularAcceleration: _VectorIn3D
                 ) -> None:
        IObject.numberOfObjects += 1
        self.mass = mass  # Mass of the object
        self.originCoordinates = originCoordinates  # Position of origin of coordinate system defining object
        self.rotationMatrix = rotationMatrix  # Rotation matrix composed of vectors defining local coordinate system
        self.velocityMatrix = velocityMatrix  # [X, Y, Z] components of velocity in local coordinate system
        self.accelerationMatrix = accelerationMatrix  # [X, Y, Z] components of acceleration in local coordinate system
        self.momentOfInertiaMatrix = momentOfInertiaMatrix  # [X, Y, Z] components of moment of inertia around object axis of local coordinate system
        self.angularVelocity = angularVelocity  # [X, Y, Z] components of angular velocity of object axis of local coordinate system
        self.angularAcceleration = angularAcceleration  # [X, Y, Z] components of angular acceleration of object axis of local coordinate system

