from .calculator_1 import Calculator1
from typing import Dict

class MockRequest:
    def __init__(self, body: Dict ) -> None:
        self.json = body

def test_calculate():

    mock_request = MockRequest(body={"number": 1})

    calculator_1 = Calculator1()

    answer = calculator_1.calculate(mock_request)
    
    assert "data" in answer
    assert "Calculator" in answer["data"]
    assert "Result" in answer["data"]
