import math
from typing import List

import numpy as np
from nptyping import NDArray, Shape, Float

from Exeptions.ValueOutOfTheBoundError import ValueOutOfTheBoundError
from IObject import IObject
from Planets.IPlanetWithAtmosphere import IPlanetWithAtmosphere
from force_generarors.IAerodynamicSurface import IAerodynamicSurface


class SimpleAerodynamicSurface(IAerodynamicSurface):
    """simple flat plate aerodynamic surface"""

    def __init__(self,
                 surfaceLocation: IObject.VectorIn3D,
                 objectToActForceOn: IObject,
                 planetWithAtmosphere: IPlanetWithAtmosphere,
                 axisOfRotation: IObject.VectorIn3D,
                 maxAngleOfDeflectionInDegrees: float,
                 areaOfTheAeroSurface: float) -> None:
        super().__init__(surfaceLocation,
                         objectToActForceOn,
                         planetWithAtmosphere)
        self.axisOfRotation: IObject.VectorIn3D = axisOfRotation
        self.deflection: List[float] = [0]
        if maxAngleOfDeflectionInDegrees < 0:
            raise ValueOutOfTheBoundError(maxAngleOfDeflectionInDegrees, 0, float('inf'))
        self.maxAngleOfDeflectionInRadians: float = math.radians(maxAngleOfDeflectionInDegrees)
        self.normalVectorToAeroSurfaceAtZeroDeflection: IObject.VectorIn3D = np.cross(
            self.objectToActForceOn.currentRotationMatrix[:, 0],
            np.matmul(self.objectToActForceOn.currentRotationMatrix, self.axisOfRotation))
        self.vectorAlongAeroSurfaceAtZeroDeflection: IObject.VectorIn3D = np.cross(self.axisOfRotation,
                                                                                   self.normalVectorToAeroSurfaceAtZeroDeflection)
        self.areaOfTheAeroSurface: float = areaOfTheAeroSurface

    def setDeflection(self, deflection: float) -> None:
        super().setDeflection(deflection)
        self.deflection.append(deflection)

    def getForce(self) -> IObject.VectorIn3D:
        current_relative_air_velocity: IObject.VectorIn3D = self.getRelativeVelocityVector()
        normal_to_aero_surface_component_of_air_velocity: float = float(np.linalg.norm(
            self.__projectVectorUOnVectorV(current_relative_air_velocity,
                                           self.normalVectorToAeroSurfaceAtZeroDeflection)))
        along_aero_surface_component_of_air_velocity: float = float(np.linalg.norm(
            self.__projectVectorUOnVectorV(current_relative_air_velocity,
                                           self.vectorAlongAeroSurfaceAtZeroDeflection)))

        angle_of_attack: float = math.atan(normal_to_aero_surface_component_of_air_velocity/along_aero_surface_component_of_air_velocity)
        angle_of_attack += self.__getDeflectionAngle()

        lift_coefficient: float = 2*math.pi*angle_of_attack
        air_density = self.planetWithAtmosphere.getAirDensity(self.planetWithAtmosphere.getAltitude(self.objectToActForceOn))
        lift_force: float = 0.5 * air_density * self.areaOfTheAeroSurface * lift_coefficient * (normal_to_aero_surface_component_of_air_velocity**2 + along_aero_surface_component_of_air_velocity**2)

        lift_vector: IObject.VectorIn3D = np.cross(self.axisOfRotation, current_relative_air_velocity)
        lift_vector = lift_vector / np.linalg.norm(lift_vector)

        return lift_force * lift_vector

    def getMoment(self) -> IObject.VectorIn3D:
        return np.cross(np.matmul(self.objectToActForceOn.currentRotationMatrix, self.getPositionForceActThrough()), self.getForce())

    def getDeflection(self) -> float:
        return self.deflection[-1]

    @staticmethod
    def __projectVectorUOnVectorV(u: IObject.VectorIn3D, v: IObject.VectorIn3D) -> IObject.VectorIn3D:
        a: IObject.VectorIn3D = (np.dot(u, v) / np.dot(v, v)) * v
        return a

    def __getDeflectionAngle(self) -> float:
        return self.deflection[-1] * self.maxAngleOfDeflectionInRadians
