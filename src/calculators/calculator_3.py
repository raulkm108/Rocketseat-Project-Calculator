from src.drivers.interfaces.driver_handler_interface import VarianceDriverHandlerInterface, MultiplyDriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List


class Calculator3:
    def __init__(self, variance_driver_handler: VarianceDriverHandlerInterface, multiply_driver_handler: MultiplyDriverHandlerInterface) -> None:
        self.__variance_driver_handler = variance_driver_handler
        self.__multiply_driver_handler = multiply_driver_handler
        pass

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        validated_response = self.__validate_body(body)
        comparison_response = self.__multiplication_variance_comparison(validated_response)
        edited_final_result = self.__format_response(comparison_response)
        return edited_final_result
    
    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("Wrong body format!")

        if len(body["numbers"]) < 2:
            raise Exception("You need 2 numbers or more!")
            
        input_data = body["numbers"]
        return input_data

    def __multiplication_variance_comparison(self, input_data: List) -> bool:
        variance = self.__variance_driver_handler.make_variance(input_data)
        multiplication = self.__multiply_driver_handler.make_multiply(input_data)
        if variance < multiplication:
            return "Positive"
        else:
            return "Negative"
        
    def __format_response(self, comparison_response: str) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "Result": comparison_response
            }
        }
