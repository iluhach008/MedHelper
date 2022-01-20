from flask import jsonify, request
from . import routes
from service import cabinetService
from exception.cabinetException import *
from exception.baseException import *
import json


# Получение по номеру кабинета
@routes.route('/cabinet/<int:number>', methods=['GET'])
def get_cabinet(number):
    try:
        return jsonify(cabinetService.getByNumber(number))
    except Exception as ex:
        if isinstance(ex, NotFoundException):
            return "Ошибка. Кабинет не найден [1]", 404
        else:
            print(ex)
            return "Ошибка", 400


# Добавление кабинета
@routes.route('/cabinet', methods=['POST'])
def create():
    if request.data:
        try:
            return jsonify(cabinetService.create(json.loads(request.data)))
        except Exception as ex:
            if isinstance(ex, NotEnoughDataException):
                return "Ошибка. Недостаточно данных [2]", 400
            elif isinstance(ex, IncorrectDataException):
                return "Ошибка. Некоректные данные [3]", 400
            elif isinstance(ex, CabinetAlreadyException):
                return "Ошибка. Кабинет с таким номером уже существует [4]", 400
            else:
                print(ex)
                return "Ошибка", 400
    else:
        return "Ошибка. Недостаточно данных. [1]", 400


# Редактирование кабинета
@routes.route('/cabinet/<int:number>', methods=['PUT'])
def update_cabinet(number):
    if request.data:
        try:
            return jsonify(cabinetService.update(number, json.loads(request.data)))
        except Exception as ex:
            if isinstance(ex, NotEnoughDataException):
                return "Ошибка. Недостаточно данных [2]", 400
            elif isinstance(ex, IncorrectDataException):
                return "Ошибка. Некоректные данные [3]", 400
            elif isinstance(ex, CabinetAlreadyException):
                return "Ошибка. Кабинет с таким номером уже существует [4]", 400
            else:
                print(ex)
                return "Ошибка", 400
    else:
        return "Ошибка. Недостаточно данных. [1]", 400


# Получение списка этажей кабинетов
@routes.route('/floors', methods=['GET'])
def get_floors():
    return jsonify(cabinetService.getFloors())


# Получение списка кабинетов
@routes.route('/cabinetsShort', methods=['GET'])
def get_cabinetsShort():
    return jsonify(cabinetService.getAllshort())


# Получение кабинетов
@routes.route('/cabinets', methods=['GET'])
def get_cabinets():
    return jsonify(cabinetService.getAll())


# Удаление кабинета
@routes.route('/cabinet/<int:number>', methods=['DELETE'])
def delete_cabinet(number):
    try:
        return jsonify(cabinetService.deleteByNumber(number))
    except Exception as ex:
        if isinstance(ex, NotFoundException):
            return "Ошибка. Кабинет не найден [1]", 404
        else:
            print(ex)
            return "Ошибка", 400