from exception import baseException, cabinetException
from dal import cabinetDal


# Получение кабиента по номеру
def getByNumber(number):
    cabinet = cabinetDal.getByNumber(number)
    return cabinet


# Добавление кабинета
def create(data):
    # Проверка на совпадение типа данных
    if type(data) == dict:
        keys = set(data.keys())
        need_keys = {'name', 'number', 'floor'}
        # Проверка на наличие необходимых данных
        if not need_keys.issubset(keys):
            raise baseException.NotEnoughDataException
        # Проверка на пустоту данных
        if  not data['name'] or\
            not data['number'] or\
            not data['floor']:
            raise baseException.NotEnoughDataException

        # Проверка этажа и номера на коректность
        if not str(data['number']).isnumeric() or not str(data['floor']).isnumeric():
            raise baseException.IncorrectDataException

        # Проверка на доступность номера
        if getByNumber(data['number']):
            raise cabinetException.CabinetAlreadyException

        # Добавление кабиента
        return cabinetDal.create(data)
    else:
        raise baseException.NotEnoughDataException


# Редактирование кабинета
def update(number, data):
    # Проверка на совпадение типа данных
    if type(data) == dict:
        keys = set(data.keys())
        need_keys = {'name', 'number', 'floor'}
        # Проверка на наличие необходимых данных
        if not need_keys.issubset(keys):
            raise baseException.NotEnoughDataException
        # Проверка на пустоту данных
        if  not data['name'] or\
            not data['number'] or\
            not data['floor']:
            raise baseException.NotEnoughDataException

        # Проверка этажа и номера на коректность
        if not str(data['number']).isnumeric() or not str(data['floor']).isnumeric():
            raise baseException.IncorrectDataException

        # Проверка на доступность номера
        if data['number'] != number and getByNumber(data['number']):
            raise cabinetException.CabinetAlreadyException

        # Добавление кабиента
        return cabinetDal.update(number, data)
    else:
        raise baseException.NotEnoughDataException


# Получение кабинетов
def getAll():
    return cabinetDal.getAll()


# Получение списка кабинетов
def getAllshort():
    return cabinetDal.getAllshort()


# Получение этажей
def getFloors():
    return cabinetDal.getFloors()


# Удаление по ид
def deleteByNumber(number):
    return cabinetDal.deleteByNumber(number)