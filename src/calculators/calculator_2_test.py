from typing import Dict
from.calculator_2 import Calculator2

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest({ "numbers": [2.12, 4.62, 1.32]})

    calculator_2 = Calculator2()
    edited_value = calculator_2.calculate(mock_request)
    print()
    print(edited_value)

    assert isinstance(edited_value, dict)
    assert edited_value == {'data': {'Calculator': 2, 'Result': 0.080959}}


