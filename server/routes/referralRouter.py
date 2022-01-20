from flask import jsonify, request
from . import routes
from service import referralService
from exception.baseException import *
import json


# Получение направлений
@routes.route('/referrals', methods=['GET'])
def get_referrals():
    return jsonify(referralService.getAll())


# Получение направлений по полису
@routes.route('/referral/<int:id>', methods=['GET'])
def get_referral(id):
    return jsonify(referralService.getByPolis(id))


# Получение списка типов направлений
@routes.route('/referralTypes', methods=['GET'])
def get_referralTypes():
    return jsonify(referralService.getTypes())



# Удаление
@routes.route('/referral/<int:id>', methods=['DELETE'])
def delete_referral(id):
    try:
        return jsonify(referralService.deleteByID(id))
    except Exception as ex:
        if isinstance(ex, NotFoundException):
            return "Ошибка. Запись не найдена [1]", 404
        else:
            print(ex)
            return "Ошибка", 400