from exception import baseException, patientException
from re import fullmatch
from dal import patientDal


# Получение пациентов
def getAll():
    return patientDal.getAll()


# Регистрация пациентов
def register(data):
    # Проверка на совпадение типа данных
    if type(data) == dict:
        keys = set(data.keys())
        need_keys = {'address', 'birthday','fathername','gender','name','phone','polis','surname'}
        # Проверка на наличие необходимых данных
        if not need_keys.issubset(keys):
            raise baseException.NotEnoughDataException
        # Проверка на пустоту данных
        if  not data['address'] or\
            not data['birthday'] or\
            not data['fathername'] or \
            not data['gender'] or\
            not data['name'] or\
            not data['phone'] or \
            not data['polis'] or \
            not data['surname']:
            raise baseException.NotEnoughDataException
        # Проверка на коректность номера
        if not fullmatch(r'8 \([0-9]{3}\) [0-9]{3}-[0-9]{2}-[0-9]{2}', data['phone']):
            raise baseException.IncorrectDataException
        # Проверка на коректность номера полиса
        if len(str(data['polis'])) != 16 or not fullmatch(r'^[0-9]+$', data['polis']):
            raise baseException.IncorrectDataException

        # Проверка на доступность номера полиса
        if getByPolis(data['polis']):
            raise patientException.PatientAlreadyException

        # Добавление пользователя
        return patientDal.register(data)
    else:
        raise baseException.NotEnoughDataException



# Регистрация пациентов
def update(polis, data):
    # Проверка на совпадение типа данных
    if type(data) == dict:
        keys = set(data.keys())
        need_keys = {'address', 'birthday','fathername','gender','name','phone','polis','surname'}
        # Проверка на наличие необходимых данных
        if not need_keys.issubset(keys):
            raise baseException.NotEnoughDataException
        # Проверка на пустоту данных
        if  not data['address'] or\
            not data['birthday'] or\
            not data['fathername'] or \
            not data['gender'] or\
            not data['name'] or\
            not data['phone'] or \
            not data['polis'] or \
            not data['surname']:
            raise baseException.NotEnoughDataException
        # Проверка на коректность номера
        if not fullmatch(r'8 \([0-9]{3}\) [0-9]{3}-[0-9]{2}-[0-9]{2}', data['phone']):
            raise baseException.IncorrectDataException
        # Проверка на коректность номера полиса
        if len(str(data['polis'])) != 16 or not fullmatch(r'^[0-9]+$', data['polis']):
            raise baseException.IncorrectDataException

        # Добавление пользователя
        return patientDal.update(polis, data)
    else:
        raise baseException.NotEnoughDataException



# Получение пациента по полису
def getByPolis(polis):
    return patientDal.getByPolis(polis)


# Удаление по ид
def deleteByPolis(polis):
    return patientDal.deleteByPolis(polis)