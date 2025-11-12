from typing import Dict, List
from .calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):

    def standard_derivation(self, numbers: List[float]) -> float:
        return 3
    
    def make_variance(self, numbers: List[float]) -> float:
        return 3

    def make_multiply(self, numbers: List[float]) -> float:
        return 3


def test_calculate_integration():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 50]})

    driver = NumpyHandler()
    calculator_3 = Calculator3(driver)
    edited_value = calculator_3.calculate(mock_request)
    
    print(edited_value)
    assert isinstance(edited_value, dict)
    assert edited_value == {'data': {'Calculator': 3, 'Result': "Negative"}}

def test_calculate():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 50]})

    driver = MockDriverHandler()
    calculator_3 = Calculator3(driver)
    edited_value = calculator_3.calculate(mock_request)
    
    print(edited_value)
    assert isinstance(edited_value, dict)
    assert edited_value == {'data': {'Calculator': 3, 'Result': "Negative"}}


