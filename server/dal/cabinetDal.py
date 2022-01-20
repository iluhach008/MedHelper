from . import cursor, conn


def getByNumber(number):
    cursor.execute(f'SELECT * FROM cabinet WHERE number = {number}')
    records = cursor.fetchone()
    return records


def create(data):
    cursor.execute(f"INSERT INTO cabinet "
                   f"(name, number, floor) VALUES "
                   f"('{data['name']}', '{data['number']}', '{data['floor']}') RETURNING number")
    records = cursor.fetchone()
    conn.commit()
    return records['number']


def update(number, data):
    cursor.execute(f"UPDATE cabinet SET "
                   f"name =  '{data['name']}', "
                   f"number = '{data['number']}', "
                   f"floor = '{data['floor']}'"
                   f"WHERE number = {number} RETURNING number")
    records = cursor.fetchone()
    conn.commit()
    return records['number']


def getAll():
    cursor.execute('SELECT * FROM cabinet')
    records = cursor.fetchall()
    return records


def getAllshort():
    cursor.execute('SELECT number as "name", number as "value" FROM cabinet')
    records = cursor.fetchall()
    return records



def getFloors():
    cursor.execute('SELECT floor as "name", floor as "value" FROM cabinet GROUP BY floor ORDER BY floor')
    records = cursor.fetchall()
    return records


def deleteByNumber(number):
    cursor.execute(f'DELETE FROM cabinet WHERE number = {number}')
    conn.commit()
    return True