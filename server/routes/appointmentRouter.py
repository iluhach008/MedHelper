from flask import jsonify, request
from . import routes
from service import appointmentService
from exception.baseException import *
from exception.appointmentException import *
import json

# Добавление записи к врачу
@routes.route('/appointment', methods=['POST'])
def create_appointment():
    if request.data:
        try:
            return jsonify(appointmentService.create(json.loads(request.data)))
        except Exception as ex:
            if isinstance(ex, NotEnoughDataException):
                return "Ошибка. Недостаточно данных [2]", 400
            elif isinstance(ex, IncorrectDataException):
                return "Ошибка. Некоректные данные [3]", 400
            elif isinstance(ex, TimeCrossingException):
                return "Ошибка. Выбранное время занято [4]", 400
            else:
                print(ex)
                return "Ошибка", 400
    else:
        return "Ошибка. Недостаточно данных. [1]", 400

# Получение записей к врачу
@routes.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify(appointmentService.getAll())


# Получение по id
@routes.route('/appointment/<int:id>', methods=['GET'])
def get_appointment(id):
    try:
        return jsonify(appointmentService.getByID(id))
    except Exception as ex:
        if isinstance(ex, NotFoundException):
            return "Ошибка. Запись не найдена не найден [1]", 404
        else:
            print(ex)
            return "Ошибка", 400


# Удаление
@routes.route('/appointment/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    try:
        return jsonify(appointmentService.deleteByID(id))
    except Exception as ex:
        if isinstance(ex, NotFoundException):
            return "Ошибка. Запись не найдена [1]", 404
        else:
            print(ex)
            return "Ошибка", 400