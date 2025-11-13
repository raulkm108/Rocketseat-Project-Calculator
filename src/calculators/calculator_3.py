from src.drivers.interfaces.driver_handler_interface import VarianceDriverHandlerInterface, MultiplyDriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator3:
    def __init__(self, variance_driver_handler: VarianceDriverHandlerInterface, multiply_driver_handler: MultiplyDriverHandlerInterface) -> None:
        self.__variance_driver_handler = variance_driver_handler
        self.__multiply_driver_handler = multiply_driver_handler
        pass

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        validated_response = self.__validate_body(body)
        variance = self.__calculate_variance(validated_response)
        multiplication = self.__calculate_multiplication(validated_response)
        comparison_response = self.__multiplication_variance_comparison(variance, multiplication)
        edited_final_result = self.__format_response(comparison_response)
        return edited_final_result
    
    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Wrong body format!")

        if len(body["numbers"]) < 2:
            raise HttpUnprocessableEntityError("You need 2 numbers or more!")
            
        input_data = body["numbers"]
        return input_data

    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__variance_driver_handler.make_variance(numbers)
        return variance
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = self.__multiply_driver_handler.make_multiply(numbers)
        return multiplication


    def __multiplication_variance_comparison(self, variance: float, multiplication: float) -> str:
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
