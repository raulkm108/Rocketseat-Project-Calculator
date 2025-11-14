from src.drivers.interfaces.driver_handler_interface import ArithmeticMeanDriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
    def __init__(self, arithmetic_mean_driver_handler: ArithmeticMeanDriverHandlerInterface) -> None:
        self.__arithmetic_mean_driver_handler = arithmetic_mean_driver_handler
        pass

    def calculate(self, request: FlaskRequest) -> Dict: # type:ignore
        body = request.json
        validated_response = self.__validate_body(body)
        arithmetic_mean = self.__calculate_arithmetic_mean(validated_response)
        edited_final_result = self.__format_response(arithmetic_mean)
        return edited_final_result

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Wrong body format!")

        if len(body["numbers"]) < 2:
            raise HttpUnprocessableEntityError("You need 2 numbers or more!")
            
        input_data = body["numbers"]
        return input_data
    
    def __calculate_arithmetic_mean(self, numbers: List[float]) -> float:
        arithmetic_mean = self.__arithmetic_mean_driver_handler.make_arithmetic_mean(numbers)
        return arithmetic_mean

    def __format_response(self, arithmetic_mean: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "Result": arithmetic_mean
            }
        }