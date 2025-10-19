from flask import Flask, Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1
from src.calculators.calculator_2 import Calculator2

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=['POST'])
def calculator_1():
    calc = Calculator1()
    final_result = calc.calculate(request)

    return jsonify (final_result)

@calc_route_bp.route("/calculator/2", methods=['POST'])
def calculator_2():
    calc = Calculator2()
    final_result = calc.calculate(request)

    return jsonify (final_result)
