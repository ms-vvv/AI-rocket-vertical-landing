from abc import abstractmethod
from abc import ABC

from IObject import IObject


class IForceGenerator(ABC):
    """Interface defining object generating force on IObject"""

    def __init__(self,
                 forceGeneratorPosition: IObject.VectorIn3D,
                 objectToActForceOn: IObject) -> None:
        self.forceGeneratorPosition: IObject.VectorIn3D = forceGeneratorPosition
        self.objectToActForceOn = objectToActForceOn

    @abstractmethod
    def getForce(self) -> IObject.VectorIn3D:
        pass
    
    @abstractmethod
    def getMoment(self) -> IObject.VectorIn3D:
        pass
    
