from flask import jsonify, request
from . import routes
from service import loginService
from flask_cors import cross_origin
from exception.baseException import *
from exception.loginException import *
import json


@routes.route('/login', methods=['POST'])
@cross_origin()
def login():
    if request.data:
        try:
            return jsonify(loginService.login(json.loads(request.data)))
        except Exception as ex:
            if isinstance(ex, NotEnoughDataException):
                return "Ошибка. Недостаточно данных [2]", 400
            elif isinstance(ex, IncorrectDataException):
                return "Ошибка. Некоректные данные [3]", 400
            elif isinstance(ex, InvalidLoginOrPasswordException):
                return "Ошибка. Пользователь с таким логином и паролем не существует [4]", 400
            else:
                print(ex)
                return "Ошибка", 400
    else:
        return "Ошибка. Недостаточно данных. [1]", 400

@routes.route('/checklogin', methods=['POST'])
@cross_origin()
def checkLogin():
    if request.data:
        try:
            return jsonify(loginService.checkLogin(json.loads(request.data)))
        except Exception as ex:
            if isinstance(ex, NotEnoughDataException):
                return "Ошибка. Недостаточно данных [2]", 400
            elif isinstance(ex, IncorrectDataException):
                return "Ошибка. Некоректные данные [3]", 400
            elif isinstance(ex, AuthorizationTimeOutException):
                return "Ошибка. Время действия авторизации истекло [4]", 400
            else:
                print(ex)
                return "Ошибка", 400
    else:
        return "Ошибка. Недостаточно данных. [1]", 400