from .calculator_1 import Calculator1
from typing import Dict
from pytest import raises

class MockRequest:
    def __init__(self, body: Dict ) -> None:
        self.json = body

def test_calculate():

    mock_request = MockRequest(body={"number": 1})

    calculator_1 = Calculator1()

    answer = calculator_1.calculate(mock_request)
    
    #format of the answer
    assert "data" in answer
    assert "Calculator" in answer["data"]
    assert "Result" in answer["data"]

    #Assertiveness of the answer
    assert answer["data"]["Result"] == 14.25
    assert answer ["data"]["Calculator"] == 1

def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 1})
    calculator_1 = Calculator1()

    with raises(Exception) as excinfo:
        calculator_1.calculate(mock_request)

    assert str(excinfo.value) == "Wrong body format!"




