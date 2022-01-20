from . import cursor, conn


def getAll():
    cursor.execute('SELECT * FROM patient')
    records = cursor.fetchall()
    return records


def getByPolis(polis):
    cursor.execute(f"SELECT * FROM patient WHERE polis = '{polis}'")
    records = cursor.fetchone()
    return records


def register(data):
    cursor.execute(f"INSERT INTO patient "
                   f"(address, birthday,fathername,gender,name,phone,polis,surname) VALUES "
                   f"('{data['address']}', '{data['birthday']}', '{data['fathername']}', '{data['gender']}', "
                   f"'{data['name']}','{data['phone']}', '{data['polis']}', '{data['surname']}') RETURNING polis")
    records = cursor.fetchone()
    conn.commit()
    return records['polis']


def update(polis, data):
    cursor.execute(f"UPDATE patient SET "
                   f"address ='{data['address']}', "
                   f"birthday ='{data['birthday']}', "
                   f"fathername ='{data['fathername']}', "
                   f"gender ='{data['gender']}', "
                   f"name ='{data['name']}', "
                   f"phone ='{data['phone']}', "
                   f"surname ='{data['surname']}' "
                   f"WHERE polis = '{polis}' RETURNING polis")
    records = cursor.fetchone()
    conn.commit()
    return records['polis']


def deleteByPolis(polis):
    cursor.execute(f"DELETE FROM patient WHERE polis = '{polis}'")
    cursor.execute(f"DELETE FROM appointment WHERE patient = '{polis}'")
    cursor.execute(f"DELETE FROM doctorvisit WHERE patient = '{polis}'")
    cursor.execute(f"DELETE FROM labresult WHERE patient = '{polis}'")
    cursor.execute(f"DELETE FROM referral WHERE patient = '{polis}'")
    conn.commit()
    return True