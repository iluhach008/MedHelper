from exception import baseException, timetableException
from service import employeeService
from service import specializationService
from dal import timetbelDal


# Добавление расписания
def create(data):
    # Проверка на совпадение типа данных
    if type(data) == dict:
        keys = set(data.keys())
        need_keys = {'employee', 'datebefore','datefrom','interval','timebefore','timefrom'}
        # Проверка на наличие необходимых данных
        if not need_keys.issubset(keys):
            raise baseException.NotEnoughDataException
        # Проверка на пустоту данных
        if  not data['employee'] or\
            not data['datebefore'] or\
            not data['datefrom'] or \
            not data['interval'] or\
            not data['timebefore'] or\
            not data['timefrom']:
            raise baseException.NotEnoughDataException
        # Проверка на существание сотрудника
        if not str(data['employee']).isnumeric() or not employeeService.getOneByID(data['employee']):
            raise baseException.IncorrectDataException
        # Проверка на наличие пересечения
        if checkTimeCrossing(data['datefrom'], data['datebefore'], data['employee']):
            raise timetableException.TimeCrossingException

        # Добавление расписания
        return timetbelDal.create(data)
    else:
        raise baseException.NotEnoughDataException


# Проверка пересечения true - пересечение есть
def checkTimeCrossing(tStart, tEnd, employeeID):
    if timetbelDal.checkTimeCrossing(tStart, tEnd, employeeID):
        return True
    else:
        return False


# Получение расписания по сотруднику
def getByEmployee(id):
    cabinet = timetbelDal.getByEmployee(id)
    return cabinet


# Получение расписаний
def getAll():
    timetbels = specializationService.getAllSimple()
    for i in timetbels:
        i['doctors'] = employeeService.getAllBySpecialization(i['id'])
        for j in i['doctors']:
            j['timetabel'] = getByEmployee(j['id'])

    return timetbels

# Удаление по ид
def deleteByID(id):
    return timetbelDal.deleteByID(id)