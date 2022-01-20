from exception import baseException, appointmentException
from dal import appointmentDal

# Добавление кабинета
def create(data):
    # Проверка на совпадение типа данных
    if type(data) == dict:
        keys = set(data.keys())
        need_keys = {'date', 'doctor', 'patient', 'time'}
        # Проверка на наличие необходимых данных
        if not need_keys.issubset(keys):
            raise baseException.NotEnoughDataException
        # Проверка на пустоту данных
        if  not data['date'] or\
            not data['doctor'] or\
            not data['patient']or\
            not data['time']:
            raise baseException.NotEnoughDataException

        # Проверка на слота
        if checkTimeCrossing(data['date'], data['time'],data['doctor']):
            raise appointmentException.TimeCrossingException

        # Добавление кабиента
        return appointmentDal.create(data)
    else:
        raise baseException.NotEnoughDataException



# Проверка пересечения true - пересечение есть
def checkTimeCrossing(date, time, doctor):
    if appointmentDal.checkTimeCrossing(date, time, doctor):
        return True
    else:
        return False


# Получение записей
def getAll():
    return appointmentDal.getAll()


# Получение записей
def getByID(id):
    return appointmentDal.getByID(id)


# Получение записей
def setStatusFalse(id):
    return appointmentDal.setStatusFalse(id)


# Удаление по ид
def deleteByID(id):
    return appointmentDal.deleteByID(id)