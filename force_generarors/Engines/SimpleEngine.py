import math
from typing import List

import numpy as np

from IObject import IObject
from force_generarors.IEngine import IEngine


class SimpleEngine(IEngine):

    def __init__(self,
                 forceGeneratorPosition: IObject.VectorIn3D,
                 engineAxis: IObject.VectorIn3D,
                 objectToActForceOn: IObject,
                 maxGimbalPitchAngleInDegrees: float,
                 maxGimbalYawAngleInDegrees: float,
                 pitchAxisVector: IObject.VectorIn3D,
                 maxThrustInNewtons: float,
                 minThrustInNewtons: float):
        super().__init__(forceGeneratorPosition,
                         objectToActForceOn)
        self.maxGimbalPitchAngleInRadians: float = math.radians(maxGimbalPitchAngleInDegrees)
        self.maxGimbalYawAngleInRadians: float = math.radians(maxGimbalYawAngleInDegrees)
        self.engineAxis: IObject.VectorIn3D = engineAxis / np.linalg.norm(engineAxis)
        self.gimbalPitchDeflection: List[float] = [0]
        self.gimbalYawDeflection: List[float] = [0]
        self.thrustLevel: List[float] = [0]
        self.yawVector: IObject.VectorIn3D = np.cross(self.engineAxis, pitchAxisVector)
        self.yawVector = self.yawVector / np.linalg.norm(self.yawVector)
        self.pitchVector: IObject.VectorIn3D = np.cross(self.yawVector, self.engineAxis)
        self.pitchVector = self.pitchVector/np.linalg.norm(self.pitchVector)
        self.maxThrustInNewtons: float = maxThrustInNewtons
        self.minThrustInNewtons: float = minThrustInNewtons

    def setGimbalDeflection(self, deflectionInPitch: float, deflectionInYaw: float) -> None:
        self.gimbalPitchDeflection.append(deflectionInPitch)
        self.gimbalYawDeflection.append(deflectionInYaw)

    def getGimbalPitchDeflection(self) -> float:
        return self.gimbalPitchDeflection[-1]

    def getGimbalYawDeflection(self) -> float:
        return self.gimbalYawDeflection[-1]

    def setThrustLevel(self, thrustLevel: float) -> None:
        self.thrustLevel.append(thrustLevel)

    def getThrustLevel(self) -> float:
        return self.thrustLevel[-1]

    def getForce(self) -> IObject.VectorIn3D:
        pitch_deflection_vector: IObject.VectorIn3D = math.tan(self.__getPitchAngle()) * self.yawVector
        yaw_deflection_vector: IObject.VectorIn3D = math.tan(self.__getYawAngle()) * self.pitchVector
        force_vector: IObject.VectorIn3D = self.engineAxis + pitch_deflection_vector + yaw_deflection_vector
        force_vector = force_vector / np.linalg.norm(force_vector)

        return np.matmul(self.objectToActForceOn.currentRotationMatrix, force_vector * self.__getThrustForce())

    def getMoment(self) -> IObject.VectorIn3D:
        return np.zeros(3)

    def __getPitchAngle(self) -> float:
        return self.maxGimbalPitchAngleInRadians * self.gimbalPitchDeflection[-1]

    def __getYawAngle(self) -> float:
        return self.maxGimbalYawAngleInRadians * self.gimbalYawDeflection[-1]

    def __getThrustForce(self) -> float:
        if self.thrustLevel[-1] == 0:
            return 0
        return self.minThrustInNewtons + (self.maxThrustInNewtons - self.minThrustInNewtons)*self.thrustLevel[-1]
    