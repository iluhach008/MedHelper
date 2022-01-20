from exception import baseException
from service import referralService
from dal import labReultDal


# Добавление реузльтат лабораторных исследований
def create(data):
    # Проверка на совпадение типа данных
    if type(data) == dict:
        keys = set(data.keys())
        need_keys = {'referral', 'result', 'datetime', 'description'}
        # Проверка на наличие необходимых данных
        if not need_keys.issubset(keys):
            raise baseException.NotEnoughDataException
        # Проверка на пустоту данных
        if  not data['referral'] or\
            not data['result'] or\
            not data['datetime']:
            raise baseException.NotEnoughDataException
        # Полуение записи
        referral = referralService.getByID(data['referral'])
        # Добавление данных записи
        labReultID = labReultDal.create(referral, data)
        # Изменение статуса записи
        referralService.setStatusFalse(referral['id'])

        # Возврат ИД
        return labReultID
    else:
        raise baseException.NotEnoughDataException


# Добавление реузльтат лабораторных исследований
def update(id, data):
    # Проверка на совпадение типа данных
    if type(data) == dict:
        keys = set(data.keys())
        need_keys = {'referral', 'result', 'datetime', 'description'}
        # Проверка на наличие необходимых данных
        if not need_keys.issubset(keys):
            raise baseException.NotEnoughDataException
        # Проверка на пустоту данных
        if  not data['referral'] or\
            not data['result'] or\
            not data['datetime']:
            raise baseException.NotEnoughDataException

        # Добавление данных записи
        labReultID = labReultDal.update(id, data)

        # Возврат ИД
        return labReultID
    else:
        raise baseException.NotEnoughDataException

# Получение реузльтатов
def getAll():
    return labReultDal.getAll()


# Получение реузльтатов по полису
def getByPolis(polis):
    return labReultDal.getByPolis(polis)

# Получение реузльтатов по полису
def getByID(id):
    return labReultDal.getByID(id)

# Удаление по ид
def deleteByID(id):
    return labReultDal.deleteByID(id)