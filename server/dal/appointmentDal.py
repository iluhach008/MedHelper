from . import cursor, conn


def create(data):
    cursor.execute(f"INSERT INTO appointment "
                   f"(date, time, doctor, patient) VALUES "
                   f"('{data['date']}', '{data['time']}', {data['doctor']}, '{data['patient']}') RETURNING id")
    records = cursor.fetchone()
    conn.commit()
    return records['id']


# Проверка пересечения true - пересечение есть
def checkTimeCrossing(date, time, doctor):
    cursor.execute(f"SELECT * FROM appointment "
                   f"WHERE doctor = {doctor} AND date = '{date}' AND time = '{time}'")
    records = cursor.fetchall()
    return records


def getAll():
    cursor.execute('SELECT a.id, a.date, a.time, '
                   'p.name as pname, p.surname as psurname, p.fathername as pfathername, p.polis, '
                   'e.name as ename, e.surname as esurname, e.fathername as efathername '
                   'FROM appointment as a JOIN patient as p ON a.patient = p.polis JOIN employee as e ON a.doctor = e.id '
                   'WHERE a.status = true')
    records = cursor.fetchall()
    return records


def getByID(id):
    cursor.execute(f'SELECT id, doctor, patient '
                   f'FROM appointment WHERE id = {id}')
    records = cursor.fetchone()
    return records


def setStatusFalse(id):
    cursor.execute(f"UPDATE appointment SET "
                   f"status = false WHERE id = {id}")
    conn.commit()


def deleteByID(id):
    cursor.execute(f'DELETE FROM appointment WHERE id = {id}')
    conn.commit()
    return True