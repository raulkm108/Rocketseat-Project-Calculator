import numpy
from typing import List
from .interfaces.driver_handler_interface import StandardDeviationDriverHandlerInterface, VarianceDriverHandlerInterface, MultiplyDriverHandlerInterface

class NumpyHandler(StandardDeviationDriverHandlerInterface, VarianceDriverHandlerInterface, MultiplyDriverHandlerInterface):
    def __init__(self) -> None:
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers) 
    
    def make_array(self, numbers: List[float]) -> "numpy.ndarray":
        return self.__np.array(numbers) 
    
    def make_variance(self, numbers: List[float]) -> float:
        return self.__np.var(numbers)
    
    def make_multiply(self,numbers: List[float]) -> float:
        return self.__np.prod(numbers)
    
    def make_arithmetic_mean(self, numbers: List[float]) -> float:
        return self.__np.mean(numbers)