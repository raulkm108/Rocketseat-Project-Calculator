from .calculator_4 import Calculator4
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import ArithmeticMeanDriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler(ArithmeticMeanDriverHandlerInterface):

    def make_arithmetic_mean(self, numbers: List[float]) -> float:
        return 14

def test_calculate_integration():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 50]})

    driver = NumpyHandler()
    calculator_4 = Calculator4(driver)
    edited_value = calculator_4.calculate(mock_request)
    
    print(edited_value)
    assert isinstance(edited_value, dict)
    assert edited_value == {'data': {'Calculator': 4, 'Result': 14}}

def test_calculate():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 50]})

    driver = MockDriverHandler()
    calculator_4 = Calculator4(driver)
    edited_value = calculator_4.calculate(mock_request)
    
    print(edited_value)
    assert isinstance(edited_value, dict)
    assert edited_value == {'data': {'Calculator': 4, 'Result': 14}}
