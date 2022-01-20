from flask import jsonify, request
from . import routes
from service import employeeService
from exception.employeeException import *
from exception.baseException import *
import json


# Получение сотрудников
@routes.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employeeService.getAll())


# Получение по ид сотрудника
@routes.route('/employee/<int:id>', methods=['GET'])
def get_employee(id):
    try:
        return jsonify(employeeService.getOneByID(id))
    except Exception as ex:
        if isinstance(ex, NotFoundException):
            return "Ошибка. Пользователь не найден [1]", 404
        else:
            print(ex)
            return "Ошибка", 400


# Редактирование сотрудника
@routes.route('/employee/<int:id>', methods=['PUT'])
def update_employee(id):
    if request.data:
        try:
            return jsonify(employeeService.update(id, json.loads(request.data)))
        except Exception as ex:
            if isinstance(ex, NotEnoughDataException):
                return "Ошибка. Недостаточно данных [2]", 400
            elif isinstance(ex, IncorrectDataException):
                return "Ошибка. Некоректные данные [3]", 400
            elif isinstance(ex, EmployeeAlreadyException):
                return "Ошибка. Пользователь с таким логином уже существует [4]", 400
            else:
                print(ex)
                return "Ошибка", 400
    else:
        return "Ошибка. Недостаточно данных. [1]", 400


# Удаление сотрудника
@routes.route('/employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    try:
        return jsonify(employeeService.deleteByID(id))
    except Exception as ex:
        if isinstance(ex, NotFoundException):
            return "Ошибка. Пользователь не найден [1]", 404
        else:
            print(ex)
            return "Ошибка", 400


# Добавление сотрудника
@routes.route('/employee', methods=['POST'])
def register():
    if request.data:
        try:
            return jsonify(employeeService.register(json.loads(request.data)))
        except Exception as ex:
            if isinstance(ex, NotEnoughDataException):
                return "Ошибка. Недостаточно данных [2]", 400
            elif isinstance(ex, IncorrectDataException):
                return "Ошибка. Некоректные данные [3]", 400
            elif isinstance(ex, EmployeeAlreadyException):
                return "Ошибка. Пользователь с таким логином уже существует [4]", 400
            else:
                print(ex)
                return "Ошибка", 400
    else:
        return "Ошибка. Недостаточно данных. [1]", 400