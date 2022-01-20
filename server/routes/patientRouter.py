from flask import jsonify, request
from . import routes
from service import patientService
from exception.baseException import *
from exception.patientException import *
import json


# Получение пациентов
@routes.route('/patients', methods=['GET'])
def get_patients():
    return jsonify(patientService.getAll())


# Получение по полису пациента
@routes.route('/patient/<int:polis>', methods=['GET'])
def get_patient(polis):
    try:
        return jsonify(patientService.getByPolis(polis))
    except Exception as ex:
        if isinstance(ex, NotFoundException):
            return "Ошибка. Пациент не найден [1]", 404
        else:
            print(ex)
            return "Ошибка", 400


# Добавление сотрудника
@routes.route('/patient', methods=['POST'])
def register_patient():
    if request.data:
        try:
            return jsonify(patientService.register(json.loads(request.data)))
        except Exception as ex:
            if isinstance(ex, NotEnoughDataException):
                return "Ошибка. Недостаточно данных [2]", 400
            elif isinstance(ex, IncorrectDataException):
                return "Ошибка. Некоректные данные [3]", 400
            elif isinstance(ex, PatientAlreadyException):
                return "Ошибка. Пациента с таким номером полиса уже существует [4]", 400
            else:
                print(ex)
                return "Ошибка", 400
    else:
        return "Ошибка. Недостаточно данных. [1]", 400


# Редактирование сотрудника
@routes.route('/patient/<int:polis>', methods=['PUT'])
def update_patient(polis):
    if request.data:
        try:
            return jsonify(patientService.update(polis, json.loads(request.data)))
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


# Удаление пациента
@routes.route('/patient/<int:polis>', methods=['DELETE'])
def delete_patient(polis):
    try:
        return jsonify(patientService.deleteByPolis(polis))
    except Exception as ex:
        if isinstance(ex, NotFoundException):
            return "Ошибка. Кабинет не найден [1]", 404
        else:
            print(ex)
            return "Ошибка", 400