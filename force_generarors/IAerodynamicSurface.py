from abc import abstractmethod

from Exeptions.ValueOutOfTheBoundError import ValueOutOfTheBoundError
from IObject import IObject
from force_generarors.IAerodynamicForces import IAerodynamicForces


class IAerodynamicSurface(IAerodynamicForces):
    """Interface defining movable aerodynamic surface"""

    @abstractmethod
    def setDeflection(self, deflection: float) -> None:
        lower_bound: float = -1
        upper_bound: float = 1
        if deflection > upper_bound or deflection < lower_bound:
            raise ValueOutOfTheBoundError(deflection, lower_bound, upper_bound)

    @abstractmethod
    def getDeflectionAngle(self) -> float:
        pass

