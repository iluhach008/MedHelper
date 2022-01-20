from . import cursor, conn


def create(referral, data):
    cursor.execute(f"INSERT INTO labresult "
                   f"(patient, referral, datetime, result, description) VALUES "
                   f"('{referral['patient']}', '{referral['id']}', "
                   f"'{data['datetime']}', '{data['result']}', '{data['description']}') RETURNING id")
    records = cursor.fetchone()
    conn.commit()
    return records['id']


def getAll():
    cursor.execute('SELECT l.*, p.name, p.surname, p.fathername, r.type '
                   'FROM labresult as l JOIN patient as p ON l.patient = p.polis JOIN referral as r ON l.referral = r.id')
    records = cursor.fetchall()
    return records


def getByPolis(id):
    cursor.execute(f"SELECT l.*, p.name, p.surname, p.fathername, r.type "
                   f"FROM labresult as l JOIN patient as p ON l.patient = p.polis JOIN referral as r ON l.referral = r.id "
                   f"WHERE l.patient = '{id}'")
    records = cursor.fetchall()
    return records


def getByID(id):
    cursor.execute(f"SELECT * FROM labresult WHERE id = {id}")
    records = cursor.fetchone()
    return records


def update(id, data):
    cursor.execute(f"UPDATE labresult SET "
                   f"datetime ='{data['datetime']}', "
                   f"result ='{data['result']}', "
                   f"description ='{data['description']}' "
                   f"WHERE id = {id} RETURNING id")
    records = cursor.fetchone()
    conn.commit()
    return records['id']


def deleteByID(id):
    cursor.execute(f'DELETE FROM labresult WHERE id = {id}')
    conn.commit()
    return True