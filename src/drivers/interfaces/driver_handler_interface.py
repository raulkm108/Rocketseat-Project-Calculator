from abc import ABC, abstractmethod
from typing import List

class StandardDeviationDriverHandlerInterface(ABC):
    @abstractmethod
    def standard_derivation(self, numbers: List[float]) -> float:
        pass

class VarianceDriverHandlerInterface(ABC):
    @abstractmethod
    def make_variance(self, numbers: List[float]) -> float:
        pass

class MultiplyDriverHandlerInterface(ABC):
    @abstractmethod
    def make_multiply(self, numbers: List[float]) -> float:
        pass