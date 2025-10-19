from typing import Dict, List
from flask import request as FlaskRequest, jsonify
import numpy as np

class Calculator2:
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        first_edited_list = self.__first_process(input_data)
        final_value = self.__second_process(first_edited_list)
        final_edited_value = self.__format_response(final_value)
        return (final_edited_value)
        
    def __validate_body(self, body: Dict) -> List[float]: 
        if "numbers" not in body:
            raise Exception("Wrong body format!")
            
        input_data = body["numbers"]
        return input_data
    
    def __first_process(self, input_data: List[float]) -> List[float]:
        new_list = []
        for value in input_data:
            new_value = (value*11)**0.95
            new_list.append(new_value)
        return new_list
    
    def __second_process(self, first_edited_list: List[float]) -> float:
        np_list = np.array(first_edited_list)
        std_dev = np.std(np_list)
        final_result = 1/std_dev
        return final_result
    
    def __format_response(self, final_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "Result": round(final_result,2)
            }
        }
