from typing import Dict
from flask import request as FlaskRequest

class Calculator1:
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        splitted_value = input_data/3
        
    def __validate_body(self, body: Dict) -> float: 
        if "number" not in body:
            raise Exception("Wrong body format!")
            
        
        input_data = body["number"]
        return input_data
    
    def __first_process(self, splitted_value: float) -> float:
        new_number = (((splitted_value/4) + 7)**2)*0.257
        return new_number