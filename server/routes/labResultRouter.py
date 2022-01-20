from flask import jsonify, request
from . import routes
from service import labResultService
from exception.labResultException import *
from exception.baseException import *
import json


# Добавление посещения врача
@routes.route('/labResult', methods=['POST'])
def create_labResult():
    if request.data:
        try:
            return jsonify(labResultService.create(json.loads(request.data)))
        except Exception as ex:
            if isinstance(ex, NotEnoughDataException):
                return "Ошибка. Недостаточно данных [2]", 400
            elif isinstance(ex, IncorrectDataException):
                return "Ошибка. Некоректные данные [3]", 400
            else:
                print(ex)
                return "Ошибка", 400
    else:
        return "Ошибка. Недостаточно данных. [1]", 400


# Получение результатов
@routes.route('/labResults', methods=['GET'])
def get_labResults():
    return jsonify(labResultService.getAll())


# Получение результатов по полису
@routes.route('/labResult/<int:id>', methods=['GET'])
def get_labResult(id):
    return jsonify(labResultService.getByPolis(id))

# Редактирование сотрудника
@routes.route('/labResult/<int:id>', methods=['PUT'])
def update_labResult(id):
    if request.data:
        try:
            return jsonify(labResultService.update(id, json.loads(request.data)))
        except Exception as ex:
            if isinstance(ex, NotEnoughDataException):
                return "Ошибка. Недостаточно данных [2]", 400
            elif isinstance(ex, IncorrectDataException):
                return "Ошибка. Некоректные данные [3]", 400
            else:
                print(ex)
                return "Ошибка", 400
    else:
        return "Ошибка. Недостаточно данных. [1]", 400

# Получение результатов по id
@routes.route('/labResult2/<int:id>', methods=['GET'])
def get_labResult2(id):
    return jsonify(labResultService.getByID(id))



# Удаление
@routes.route('/labResult/<int:id>', methods=['DELETE'])
def delete_labResult(id):
    try:
        return jsonify(labResultService.deleteByID(id))
    except Exception as ex:
        if isinstance(ex, NotFoundException):
            return "Ошибка. Запись не найдена [1]", 404
        else:
            print(ex)
            return "Ошибка", 400