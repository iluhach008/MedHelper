from flask import jsonify, request
from . import routes
from service import timetabelService
from exception.baseException import *
from exception.timetableException import *
import json


# Добавление расписания
@routes.route('/timetabel', methods=['POST'])
def create_timetable():
    if request.data:
        try:
            return jsonify(timetabelService.create(json.loads(request.data)))
        except Exception as ex:
            if isinstance(ex, NotEnoughDataException):
                return "Ошибка. Недостаточно данных [2]", 400
            elif isinstance(ex, IncorrectDataException):
                return "Ошибка. Некоректные данные [3]", 400
            elif isinstance(ex, TimeCrossingException):
                return "Ошибка. Пересечение по времени [4]", 400
            else:
                print(ex)
                return "Ошибка", 400
    else:
        return "Ошибка. Недостаточно данных. [1]", 400


# Получение по сотруднику
@routes.route('/timetabel/<int:id>', methods=['GET'])
def get_timetabel(id):
    try:
        return jsonify(timetabelService.getByEmployee(id))
    except Exception as ex:
        if isinstance(ex, NotFoundException):
            return "Ошибка. Расписание не найдено [1]", 404
        else:
            print(ex)
            return "Ошибка", 400


# Получение расписаний
@routes.route('/timetabels', methods=['GET'])
def get_timetabels():
    try:
        return jsonify(timetabelService.getAll())
    except Exception as ex:
        if isinstance(ex, NotFoundException):
            return "Ошибка. Расписание не найдено [1]", 404
        else:
            print(ex)
            return "Ошибка", 400

# Удаление
@routes.route('/timetabel/<int:id>', methods=['DELETE'])
def delete_timetabel(id):
    try:
        return jsonify(timetabelService.deleteByID(id))
    except Exception as ex:
        if isinstance(ex, NotFoundException):
            return "Ошибка. Запись не найдена [1]", 404
        else:
            print(ex)
            return "Ошибка", 400