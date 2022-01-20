from . import cursor, conn


def create(patient, doctorVisit, data):
    cursor.execute(f"INSERT INTO referral "
                   f"(patient, doctorVisit, datetime, cabinet, type, description) VALUES "
                   f"('{patient}', {doctorVisit}, '{data['datetime']}', "
                   f"{data['cabinet']}, '{data['type']}', '{data['description']}') RETURNING id")
    records = cursor.fetchone()
    conn.commit()
    return records['id']


def getTypes():
    cursor.execute('SELECT type as "name", type as "value" FROM referral GROUP BY type ORDER BY type')
    records = cursor.fetchall()
    return records


def getAll():
    cursor.execute('SELECT r.*, p.name, p.surname, p.fathername '
                   'FROM referral as r JOIN patient as p ON r.patient = p.polis '
                   'WHERE status = true')
    records = cursor.fetchall()
    return records


def getByID(id):
    cursor.execute(f'SELECT id, patient '
                   f'FROM referral WHERE id = {id}')
    records = cursor.fetchone()
    return records


def getByPolis(id):
    cursor.execute(f"SELECT * "
                   f"FROM referral WHERE patient = '{id}'")
    records = cursor.fetchall()
    return records


def setStatusFalse(id):
    cursor.execute(f"UPDATE referral SET "
                   f"status = false WHERE id = {id}")
    conn.commit()


def deleteByID(id):
    cursor.execute(f'DELETE FROM referral WHERE id = {id}')
    conn.commit()
    return True