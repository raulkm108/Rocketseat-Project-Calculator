from flask import Flask, Blueprint, jsonify, request
from src.main.factories.calculator1_factory import calculator1_factory
from src.main.factories.calculator2_factory import calculator2_factory
from src.main.factories.calculator3_factory import calculator3_factory

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=['POST'])
def calculator_1():
    calc = calculator1_factory()
    final_result = calc.calculate(request)

    return jsonify (final_result)

@calc_route_bp.route("/calculator/2", methods=['POST'])
def calculator_2():

    calc = calculator2_factory()
    final_result = calc.calculate(request)

    return jsonify (final_result)

@calc_route_bp.route("/calculator/3", methods=['POST'])
def calculator_3():

    calc = calculator3_factory()
    final_result = calc.calculate(request)

    return jsonify (final_result)

