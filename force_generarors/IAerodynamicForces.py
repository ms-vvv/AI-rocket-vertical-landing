from abc import ABC, abstractmethod

import numpy as np

from IObject import IObject
from Planets.IPlanetWithAtmosphere import IPlanetWithAtmosphere
from force_generarors.IForceGenerator import IForceGenerator


class IAerodynamicForces(IForceGenerator, ABC):
    def __init__(self,
                 forceGeneratorPosition: IObject.VectorIn3D,
                 objectToActForceOn: IObject,
                 planetWithAtmosphere: IPlanetWithAtmosphere) -> None:
        super().__init__(forceGeneratorPosition,
                                                                                                                                                                                                                                                                                                                            objectToActForceOn)
        self.planetWithAtmosphere = planetWithAtmosphere

    def getRelativeVelocityVector(self) -> IObject.VectorIn3D:
        """Relative velocity of air in global coordinates"""
        relative_velocity: IObject.VectorIn3D = self.objectToActForceOn.currentVelocity - self.planetWithAtmosphere.currentVelocity
        radius_vector = self.objectToActForceOn.currentOriginCoordinates - self.planetWithAtmosphere.currentOriginCoordinates
        linear_velocity_of_atmosphere: IObject.VectorIn3D = np.cross(self.planetWithAtmosphere.currentAngularVelocity, radius_vector)
        relative_velocity -= linear_velocity_of_atmosphere

        return relative_velocity
