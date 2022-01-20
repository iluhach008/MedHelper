from exception import baseException
from service import referralService, appointmentService
from dal import doctorVisitDal

# Добавление кабинета
def create(data):
    # Проверка на совпадение типа данных
    if type(data) == dict:
        keys = set(data.keys())
        need_keys = {'appointment', 'complaints', 'datetime', 'description', 'diagnosis'}
        # Проверка на наличие необходимых данных
        if not need_keys.issubset(keys):
            raise baseException.NotEnoughDataException
        # Проверка на пустоту данных
        if  not data['appointment'] or\
            not data['complaints'] or\
            not data['datetime'] or\
            not data['diagnosis']:
            raise baseException.NotEnoughDataException
        # Полуение записи
        appointment = appointmentService.getByID(data['appointment'])
        # Добавление данных записи
        doctorVisitID = doctorVisitDal.create(appointment, data)
        # Добавление направлений
        for ref in data['referrals']:
            referralService.create(appointment['patient'], doctorVisitID, ref)
        # Изменение статуса записи
        appointmentService.setStatusFalse(appointment['id'])

        # Возврат ИД
        return doctorVisitID
    else:
        raise baseException.NotEnoughDataException

# Получение кабиента по номеру
def getByPolis(id):
    visits = doctorVisitDal.getByPolis(id)
    return visits