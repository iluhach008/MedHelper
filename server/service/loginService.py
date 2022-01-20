from exception import baseException
from dal import employeeDal
from exception import loginException
from datetime import datetime, timezone,timedelta
from config import SECRET_KEY
import jwt

# Авторизация сотрудников
def login(data):
    # Проверка на совпадение типа данных
    if type(data) == dict:
        keys = set(data.keys())
        need_keys = {'login', 'password'}
        # Проверка на наличие необходимых данных
        if not need_keys.issubset(keys):
            raise baseException.NotEnoughDataException
        # Проверка на пустоту данных
        if  not data['login'] or\
            not data['password']:
            raise baseException.NotEnoughDataException

        # Проверка на совпадение пары логин-пароль
        user = employeeDal.getByLoginPassword(data['login'], data['password'])
        if not user:
            raise loginException.InvalidLoginOrPasswordException

        # Добавление данных
        user['jwt'] = jwt.encode({"exp": datetime.now(tz=timezone.utc) + timedelta(hours=8), "id": user['id'], "level": user['level']}, SECRET_KEY)
        return user
    else:
        raise baseException.NotEnoughDataException


# Проверка авторизации
def checkLogin(data):
    # Проверка на совпадение типа данных
    if type(data) == dict:
        keys = set(data.keys())
        need_keys = {'jwt'}
        # Проверка на наличие необходимых данных
        if not need_keys.issubset(keys):
            raise baseException.NotEnoughDataException
        # Проверка на пустоту данных
        if  not data['jwt']:
            raise baseException.NotEnoughDataException

        # Проверка на совпадение пары логин-пароль
        validateJWT(data['jwt'])

        # Добавление данных
        return True
    else:
        raise baseException.NotEnoughDataException


def validateJWT(jwt_str):
    try:
        date = jwt.decode(jwt_str, SECRET_KEY, algorithms=["HS256"])
    except:
        raise loginException.AuthorizationTimeOutException
    return date