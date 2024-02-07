from abc import abstractmethod

from force_generarors.IForceGenerator import IForceGenerator


class IAerodynamicSurface(IForceGenerator):
    """Interface defining movable aerodynamic surface"""

    @abstractmethod
    def setDeflectionAngle(self, deflectionAngle: float) -> None:
        pass

    @abstractmethod
    def getDeflectionAngle(self) -> float:
        pass

    @abstractmethod
    def setAirVelocity(self, airVelocity: float) -> None:
        pass

    @abstractmethod
    def setAngleOfAttack(self, AngleOfAttack: float) -> None:
        pass
