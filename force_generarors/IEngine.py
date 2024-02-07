from abc import abstractmethod
from force_generarors.IForceGenerator import IForceGenerator


class IEngine(IForceGenerator):
    """Interface defining gimbaled rocket engine"""

    @abstractmethod
    def setGimbalAngle(self, deflectionInPitch: float, deflectionInYaw: float) -> None:
        pass

    @abstractmethod
    def getGimbalPitchAngle(self) -> float:
        pass

    @abstractmethod
    def getGimbalYawAngle(self) -> float:
        pass

    @abstractmethod
    def setThrustLevel(self, ThrustLevel: float) -> None:
        pass

    @abstractmethod
    def getThrustLevel(self) -> float:
        pass

