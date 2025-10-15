from flask import Flask
from models.calculator import Calculator

number = float(input("Choose a number: "))
obj = Calculator()
obj.all_count(number)