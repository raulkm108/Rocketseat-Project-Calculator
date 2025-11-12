from typing import Dict, List
from flask import request as FlaskRequest, jsonify
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

        pass
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        first_edited_list = self.__first_process(input_data)
        final_result = self.__second_process(first_edited_list)
        final_edited_value = self.__format_response(final_result)
        print(final_edited_value)
        return (final_edited_value)
        
    def __validate_body(self, body: Dict) -> List[float]: 
        if "numbers" not in body:
            raise Exception("Wrong body format!")

        if len(body["numbers"]) < 2:
            raise Exception("You need 2 numbers or more!")
            
        input_data = body["numbers"]
        return input_data
    
    def __first_process(self, input_data: List[float]) -> List[float]:
        new_list = []
        for value in input_data:
            new_value = (value*11)**0.95
            new_list.append(new_value)
            #Another solution would be: new_list = [(num * 11) ** 0.95 for num in input data]
            #This solves in one single line, but it's less readable
        return new_list
    
    def __second_process(self, first_edited_list: List[float]) -> float:

        std_dev = self.__driver_handler.standard_derivation(first_edited_list)
        final_result = 1/std_dev
        return final_result
    
    def __format_response(self, final_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "Result": round(float(final_result), 6)
            }
        }
