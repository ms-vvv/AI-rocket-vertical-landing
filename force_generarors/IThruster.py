from abc import abstractmethod


from force_generarors.IForceGenerator import IForceGenerator


class IThruster(IForceGenerator):
    """Interface defining thruster"""

    @abstractmethod
    def fireThruster(self, fireThruster: bool) -> None:
        """method changing state of the thruster; True-> Firing, False-> not firing"""
        pass
