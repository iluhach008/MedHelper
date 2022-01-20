from . import cursor, conn


def create(data):
    cursor.execute(f"INSERT INTO timetabel "
                   f"(datebefore, datefrom, employee, interval, timebefore, timefrom) VALUES "
                   f"('{data['datebefore']}', '{data['datefrom']}', {data['employee']}, {data['interval']},"
                   f"'{data['timebefore']}', '{data['timefrom']}') RETURNING id")
    records = cursor.fetchone()
    conn.commit()
    return records['id']


# Проверка пересечения true - пересечение есть
def checkTimeCrossing(tStart, tEnd, employeeID):
    cursor.execute(f"SELECT * FROM timetabel "
                   f"WHERE (timefrom < '{tEnd}' AND timebefore > '{tStart}' AND employee = {employeeID})")
    records = cursor.fetchall()
    return records


def getByEmployee(id):
    cursor.execute(f'SELECT * FROM timetabel WHERE employee = {id}')
    records = cursor.fetchall()
    return records

def deleteByID(id):
    cursor.execute(f'DELETE FROM timetabel WHERE id = {id}')
    conn.commit()
    return True