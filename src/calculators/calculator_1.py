from typing import Dict
from flask import request as FlaskRequest, jsonify

class Calculator1:
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        splitted_value = input_data/3
        first_value = self.__first_process(splitted_value)
        second_value = self.__second_process(splitted_value)
        third_value = self.__third_process(splitted_value)
        final_value = (first_value + second_value + third_value)
        final_value_edited = self.__format_response(final_value)
        return (final_value_edited)
       # return jsonify ({"Final value": final_value})
        
    def __validate_body(self, body: Dict) -> float: 
        if "number" not in body:
            raise Exception("Wrong body format!")
            
        
        input_data = body["number"]
        return input_data
    
    def __first_process(self, splitted_value: float) -> float:
        new_number = (((splitted_value/4) + 7)**2)*0.257
        return new_number
    
    def __second_process(self, splitted_value: float) -> float:
        new_number = ((splitted_value**2.121)/5) + 1
        return new_number
    
    def __third_process(self, splitted_value: float) -> float:
        return splitted_value
    
    def __format_response(self, final_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 1,
                "Result": final_result
            }
        }
