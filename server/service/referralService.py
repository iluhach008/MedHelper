from exception import baseException
from dal import referralDal


# Получение направлений
def getAll():
    return referralDal.getAll()


# Добавление направления
def create(patient, doctorVisit, data):
    # Проверка на совпадение типа данных
    if type(data) == dict:
        keys = set(data.keys())
        need_keys = {'cabinet', 'datetime', 'description', 'type'}
        # Проверка на наличие необходимых данных
        if not need_keys.issubset(keys):
            raise baseException.NotEnoughDataException
        # Проверка на пустоту данных
        if  not data['cabinet'] or\
            not data['datetime'] or\
            not data['description']or\
            not data['type']:
            raise baseException.NotEnoughDataException

        # Проверка этажа и номера на коректность
        if not str(data['cabinet']).isnumeric():
            raise baseException.IncorrectDataException

        # Добавление кабиента
        return referralDal.create(patient, doctorVisit, data)
    else:
        raise baseException.NotEnoughDataException


# Получение этажей
def getTypes():
    return referralDal.getTypes()


# Получение направления по ид
def getByID(id):
    return referralDal.getByID(id)

# Получение направления по полису
def getByPolis(polis):
    return referralDal.getByPolis(polis)


# Получение записей
def setStatusFalse(id):
    return referralDal.setStatusFalse(id)


# Удаление по ид
def deleteByID(id):
    return referralDal.deleteByID(id)