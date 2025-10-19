import numpy
from typing import List

class NumpyHandler:
    def __init__(self) -> None:
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers) 
    
    def make_array(self, numbers: List[float]) -> "numpy.ndarray":
        return self.__np.array(numbers) 