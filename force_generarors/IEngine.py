from abc import abstractmethod

from Exeptions.ValueOutOfTheBoundError import ValueOutOfTheBoundError
from force_generarors.IForceGenerator import IForceGenerator


class IEngine(IForceGenerator):
    """Interface defining gimbaled rocket engine"""

    @abstractmethod
    def setGimbalDeflection(self, deflectionInPitch: float, deflectionInYaw: float) -> None:
        lower_bound: float = -1
        upper_bound: float = 1
        if deflectionInPitch > upper_bound or deflectionInPitch < lower_bound:
            raise ValueOutOfTheBoundError(deflectionInPitch, lower_bound, upper_bound)
        if deflectionInYaw > upper_bound or deflectionInYaw < lower_bound:
            raise ValueOutOfTheBoundError(deflectionInYaw, lower_bound, upper_bound)

    @abstractmethod
    def getGimbalPitchDeflection(self) -> float:
        pass

    @abstractmethod
    def getGimbalYawDeflection(self) -> float:
        pass

    @abstractmethod
    def setThrustLevel(self, thrustLevel: float) -> None:
        pass

    @abstractmethod
    def getThrustLevel(self) -> float:
        pass

