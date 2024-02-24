import itertools

from IObject import IObject
from Objects.IPlanet import IPlanet
from Objects.IRocket import IRocket
import numpy as np


class SimulationController:
    def __init__(self,
                 rocket: IRocket,
                 planet: IPlanet):
        self.rocket: IRocket = rocket
        self.planet: IPlanet = planet

    def simulateTimeStep(self) -> None:

        # Calculating forces

        # Calculating moments



    @staticmethod
    def calculateGravitationalForce(object1: IObject, object2: IObject) -> IObject.VectorIn3D:
        gravitational_constant: float = 6.6743 * 10**(-11)
        distance_between_objects: float = float(np.linalg.norm(object1.currentOriginCoordinates - object2.currentOriginCoordinates))
        gravitational_force: float = gravitational_constant * (object1.mass[-1] * object2.mass[-1])/distance_between_objects**2

        return gravitational_force

    def calculateRocketForces(self) -> IObject.VectorIn3D:
        force: IObject.VectorIn3D = np.zeros(3)
        for actuator in self.rocket.forceGeneratingComponents:
            force += actuator.getForce()

        return force

    def calculateRocketMoments(self) -> IObject.VectorIn3D:
        moment: IObject.VectorIn3D = np.zeros(3)
        for actuator in self.rocket.forceGeneratingComponents:
            moment += actuator.getMoment()