from dal import employeeDal
from service import levelService, specializationService
from exception import employeeException, baseException
from re import fullmatch
from datetime import datetime


# Получение сотрудников
def getAll():
    return employeeDal.getAll()


# Получение сотрудников по специализации
def getAllBySpecialization(id):
    return employeeDal.getAllBySpecialization(id)


# Получение сотрудника по ИД
def getOneByID(id):
    employee = employeeDal.getByID(id)
    if employee:
        if employee['specialization']:
            employee['specialization'] = specializationService.getNameByID(employee['specialization'])
        employee['level'] = levelService.getByID(employee['level'])
        return employee
    else:
        raise baseException.NotFoundException


# Получение id сотрудника по логину
def getIdByLogin(login):
    return employeeDal.getIdByLogin(login)


# Регистрация сотрудников
def register(data):
    # Проверка на совпадение типа данных
    if type(data) == dict:
        keys = set(data.keys())
        need_keys = {'address', 'education','fathername','gender','level','login','name','password1','password2','phone','surname'}
        # Проверка на наличие необходимых данных
        if not need_keys.issubset(keys):
            raise baseException.NotEnoughDataException
        # Проверка на пустоту данных
        if  not data['address'] or\
            not data['education'] or\
            not data['fathername'] or \
            not data['gender'] or\
            not data['level'] or\
            not data['login'] or\
            not data['name'] or\
            not data['password1'] or\
            not data['password2'] or\
            not data['phone'] or\
            not data['surname']:
            raise baseException.NotEnoughDataException
        # Проверка на существание должности
        if not data['level'].isnumeric() or not levelService.getByID(data['level']):
            raise baseException.IncorrectDataException
        # Проверка на наличие специализации
        if int(data['level']) == 2:
            if not 'specialization' in keys:
                raise baseException.NotEnoughDataException
            if not data['specialization']:
                raise baseException.NotEnoughDataException
        # Проверка на коректность номера
        if not fullmatch(r'8 \([0-9]{3}\) [0-9]{3}-[0-9]{2}-[0-9]{2}', data['phone']):
            raise baseException.IncorrectDataException
        # Проверка на коректность логина
        if len(data['login']) < 4 or not fullmatch(r'^[a-zA-Z0-9]+$', data['login']):
            raise baseException.IncorrectDataException
        # Проверка на совпадение паролей
        if data['password1'] != data['password2']:
            raise baseException.IncorrectDataException
        # Проверка на коректность пароля
        if len(data['password1']) < 8:
            raise baseException.IncorrectDataException

        # Проверка на доступность логина
        if getIdByLogin(data['login']):
            raise employeeException.EmployeeAlreadyException

        # Добавление данных
        data['creator'] = 1
        data['created'] = datetime.now()
        # Добавление/Получение ИД специализации
        if int(data['level']) == 2:
            data['specialization'] = specializationService.getOrCreate(data['specialization'])
        else:
            data['specialization'] = "NULL"
        # Добавление пользователя
        return employeeDal.register(data)
    else:
        raise baseException.NotEnoughDataException


# Редактирование сотрудников
def update(id, data):
    # Проверка на совпадение типа данных
    if type(data) == dict:
        keys = set(data.keys())
        need_keys = {'address', 'education', 'fathername', 'gender', 'level', 'login', 'name', 'password1', 'password2',
                     'phone', 'surname'}
        # Проверка на наличие необходимых данных
        if not need_keys.issubset(keys):
            raise baseException.NotEnoughDataException
        # Проверка на пустоту данных
        if not data['address'] or \
                not data['education'] or \
                not data['fathername'] or \
                not data['gender'] or \
                not data['level'] or \
                not data['login'] or \
                not data['name'] or \
                not data['password1'] or \
                not data['password2'] or \
                not data['phone'] or \
                not data['surname']:
            raise baseException.NotEnoughDataException
        # Проверка на существание должности
        if not data['level'].isnumeric() or not levelService.getByID(data['level']):
            raise baseException.IncorrectDataException
        # Проверка на наличие специализации
        if int(data['level']) == 2:
            if not 'specialization' in keys:
                raise baseException.NotEnoughDataException
            if not data['specialization']:
                raise baseException.NotEnoughDataException
        # Проверка на коректность номера
        if not fullmatch(r'8 \([0-9]{3}\) [0-9]{3}-[0-9]{2}-[0-9]{2}', data['phone']):
            raise baseException.IncorrectDataException
        # Проверка на коректность логина
        if len(data['login']) < 4 or not fullmatch(r'^[a-zA-Z0-9]+$', data['login']):
            raise baseException.IncorrectDataException
        # Проверка на совпадение паролей
        if data['password1'] != data['password2']:
            raise baseException.IncorrectDataException
        # Проверка на коректность пароля
        if len(data['password1']) < 8:
            raise baseException.IncorrectDataException

        # Проверка на доступность логина
        loginId = getIdByLogin(data['login'])
        if loginId and loginId['id'] != id:
            raise employeeException.EmployeeAlreadyException

        # Добавление данных
        data['creator'] = 1
        data['created'] = datetime.now()
        # Добавление/Получение ИД специализации
        if int(data['level']) == 2:
            data['specialization'] = specializationService.getOrCreate(data['specialization'])
        else:
            data['specialization'] = "NULL"
        # Обновление пользователя
        return employeeDal.update(id, data)
    else:
        raise baseException.NotEnoughDataException


# Удаление по ид
def deleteByID(id):
    return employeeDal.deleteByID(id)