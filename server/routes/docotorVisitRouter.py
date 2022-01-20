from flask import jsonify, request
from . import routes
from service import docotorVisitService
from exception.doctorVisitException import *
from exception.baseException import *
import json


# Добавление посещения врача
@routes.route('/doctorVisit', methods=['POST'])
def create_doctorVisit():
    if request.data:
        try:
            return jsonify(docotorVisitService.create(json.loads(request.data)))
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



# Получение по пациенту
@routes.route('/doctorVisit/<int:id>', methods=['GET'])
def get_doctorVisit(id):
    try:
        return jsonify(docotorVisitService.getByPolis(id))
    except Exception as ex:
        if isinstance(ex, NotFoundException):
            return "Ошибка. История не найдена [1]", 404
        else:
            print(ex)
            return "Ошибка", 400