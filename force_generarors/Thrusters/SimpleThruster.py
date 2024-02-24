from typing import List

from IObject import IObject
from force_generarors.IThruster import IThruster
import numpy as np


class SimpleThruster(IThruster):
    def __init__(self,
                 thrusterAxis: IObject.VectorIn3D,
                 thrusterPulseThrust: float,
                 forceGeneratorPosition: IObject.VectorIn3D,
                 objectToActForceOn: IObject):
        super().__init__(forceGeneratorPosition,
                         objectToActForceOn)
        self.thrusterAxis: IObject.VectorIn3D = thrusterAxis / np.linalg.norm(thrusterAxis)
        self.thrusterPulseThrust: float = thrusterPulseThrust
        self.thrusterFiringState: List[bool] = [False]

    def fireThruster(self, fireThruster: bool) -> None:
        self.thrusterFiringState.append(fireThruster)

    def getForce(self) -> IObject.VectorIn3D:
        if self.thrusterFiringState[-1]:
            return np.matmul(self.objectToActForceOn.currentRotationMatrix, self.thrusterAxis * self.thrusterPulseThrust)
        return np.zeros(3)

    def getMoment(self) -> IObject.VectorIn3D:
        return np.zeros(3)
