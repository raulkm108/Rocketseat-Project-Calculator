from flask import Flask, Blueprint, jsonify, request

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=['POST'])
def calculator_1():
    pass