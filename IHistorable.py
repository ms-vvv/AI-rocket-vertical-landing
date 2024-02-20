from typing import Dict, List
from abc import abstractmethod;


class IHistorable():
    def __init__(self) -> None:
        self._history: Dict[str, List[float]] = {
            "time": [],
        };

    @abstractmethod
    def appendHistory(self, time: float) -> None:
        pass;

    def getHistory(self) -> Dict[str, List[float]]:
        return self._history
