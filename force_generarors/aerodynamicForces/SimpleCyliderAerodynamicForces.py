import math

import numpy as np
from typing_extensions import override

from Exeptions.ValueOutOfTheBoundError import ValueOutOfTheBoundError
from IObject import IObject
from Objects.IRocket import IRocket
from Planets.IPlanetWithAtmosphere import IPlanetWithAtmosphere
from Point import Point
from force_generarors.IAerodynamicForces import IAerodynamicForces


class SimpleCylinderAerodynamicForce(IAerodynamicForces):

    def __init__(self,
                 objectToActForceOn: IRocket,
                 planetWithAtmosphere: IPlanetWithAtmosphere,
                 cylinderDiameterInMeters: float,
                 cylinderLengthInMeters: float,
                 tipOfCylinderPosition: Point):

        super().__init__(tipOfCylinderPosition.pointPosition,
                         objectToActForceOn,
                         planetWithAtmosphere)
        self.cylinderDiameterInMeters: float = cylinderDiameterInMeters
        self.cylinderLengthInMeters: float = cylinderLengthInMeters
        self.referenceArea: float = 0.25 * math.pi * self.cylinderDiameterInMeters**2
        self.tipOfCylinderPosition: Point = tipOfCylinderPosition

    def getForce(self) -> IObject.VectorIn3D:
        relative_velocity: IObject.VectorIn3D = self.getRelativeVelocityVector()
        velocity_magnitude: float = float(np.linalg.norm(relative_velocity))
        vertical_axis_of_cylinder: IObject.VectorIn3D = self.objectToActForceOn.currentRotationMatrix[:, 0]
        angle_of_attack: float = math.asin(np.linalg.norm(np.cross(vertical_axis_of_cylinder, relative_velocity))/(np.linalg.norm(vertical_axis_of_cylinder) * velocity_magnitude))

        lift_coefficient: float = self.__getLiftCoefficient(angle_of_attack)
        air_density = self.planetWithAtmosphere.getAirDensity(
            self.planetWithAtmosphere.getAltitude(self.objectToActForceOn))
        lift_force: float = self.__getAeroForce(air_density, self.referenceArea, lift_coefficient, velocity_magnitude)

        drag_coefficient: float = self.__getDragCoefficient(angle_of_attack)
        drag_force: float = self.__getAeroForce(air_density, self.referenceArea, drag_coefficient, velocity_magnitude)

        drag_force_direction_vector: IObject.VectorIn3D = relative_velocity / np.linalg.norm(relative_velocity)

        lift_force_direction_vector: IObject.VectorIn3D = np.cross(relative_velocity, vertical_axis_of_cylinder)
        lift_force_direction_vector = np.cross(relative_velocity, lift_force_direction_vector)
        lift_force_direction_vector /= np.linalg.norm(lift_force_direction_vector)

        force_vector = drag_force_direction_vector * drag_force + lift_force_direction_vector * lift_force

        return force_vector

    def getMoment(self) -> IObject.VectorIn3D:
        return np.zeros(3)

    def __getLiftCoefficient(self, angleOfAttackInRadians: float) -> float:
        lift_coefficient: float = 1.7743 * angleOfAttackInRadians ** 4 + 4.0985 * angleOfAttackInRadians ** 3 - 3.6865 * angleOfAttackInRadians ** 2 + 2.5479 * angleOfAttackInRadians
        # lift_coefficient *=  # Cylinder length correction factor
        return lift_coefficient

    def __getDragCoefficient(self, angleOfAttackInRadians: float) -> float:
        drag_coefficient: float = 0.99814 * angleOfAttackInRadians ** 2 + 1.1111 * angleOfAttackInRadians + 1.0477
        # drag_coefficient *=   # Cylinder length correction factor
        return drag_coefficient

    def __getCenterOfPressureMeasuredFromLeadingEdgeInMeters(self, angleOfAttackInRadians: float) -> float:
        if angleOfAttackInRadians < 0.5*math.pi:
            angleOfAttackInRadians = 0.5*math.pi - angleOfAttackInRadians
            center_of_pressure: float = self.__getCenterOfPressureOfCylinderInMeters(angleOfAttackInRadians)
        elif 0.5*math.pi <= angleOfAttackInRadians <= math.pi:
            angleOfAttackInRadians -= 0.5*math.pi
            center_of_pressure = self.__getCenterOfPressureOfCylinderInMeters(angleOfAttackInRadians)
            center_of_pressure = 47.5 - center_of_pressure
        else:
            raise ValueOutOfTheBoundError(angleOfAttackInRadians, 0, math.pi)

        return center_of_pressure * self.cylinderLengthInMeters/47.5

    @staticmethod
    def __getCenterOfPressureOfCylinderInMeters(angleOfAttackInRadians: float) -> float:
        center_of_pressure: float = 8.284 * angleOfAttackInRadians ** 3 - 5.2981 * angleOfAttackInRadians ** 2 - 15.11 * angleOfAttackInRadians + 23.75

        return center_of_pressure

    @staticmethod
    def __getAeroForce(density: float, referenceArea: float, Coefficient: float, airVelocity: float) -> float:
        return 0.5 * density * referenceArea * Coefficient * airVelocity ** 2

    @override
    def getPositionForceActThrough(self) -> IObject.VectorIn3D:
        center_of_pressure: IObject.VectorIn3D = self.tipOfCylinderPosition.pointPosition

        relative_velocity: IObject.VectorIn3D = self.getRelativeVelocityVector()
        velocity_magnitude: float = float(np.linalg.norm(relative_velocity))
        vertical_axis_of_cylinder: IObject.VectorIn3D = self.objectToActForceOn.currentRotationMatrix[:, 0]
        angle_of_attack: float = math.pi - math.acos(np.dot(vertical_axis_of_cylinder, relative_velocity) / (
                    np.linalg.norm(vertical_axis_of_cylinder) * velocity_magnitude))

        center_of_pressure[0] -= self.__getCenterOfPressureMeasuredFromLeadingEdgeInMeters(angle_of_attack)

        return center_of_pressure


