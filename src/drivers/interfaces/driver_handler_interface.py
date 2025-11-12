from abc import ABC, abstractmethod
from typing import List

class DriverHandlerInterface(ABC):

    @abstractmethod
    def standard_derivation(self, numbers: List[float]) -> float:
        pass

    @abstractmethod
    def make_variance(self, numbers: List[float]) -> float:
        pass

    @abstractmethod
    def make_multiply(self, numbers: List[float]) -> float:
        pass