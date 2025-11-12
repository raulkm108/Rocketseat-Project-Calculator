from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List


class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
        pass

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        comparison_response = self.multiplication_variance_comparison(body)
        pass

    def multiplication_variance_comparison(self, input_data: List) -> bool:
        variance = self.__driver_handler.make_variance(input_data)
        multiplication = self.__driver_handler.make_multiply(input_data)
        if variance > multiplication:
            return "Positive"
        else:
            return "Negative"
        
    def format_response(self, comparison_response: str) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "Result": comparison_response
            }
        }
