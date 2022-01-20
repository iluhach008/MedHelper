from . import cursor, conn


def create(appointment, data):
    cursor.execute(f"INSERT INTO doctorVisit "
                   f"(patient, doctor, appointment, complaints, datetime, diagnosis, description) VALUES "
                   f"('{appointment['patient']}', '{appointment['doctor']}', '{appointment['id']}', "
                   f"'{data['complaints']}', '{data['datetime']}', '{data['diagnosis']}', '{data['description']}') RETURNING id")
    records = cursor.fetchone()
    conn.commit()
    return records['id']


def getByPolis(id):
    cursor.execute(f"SELECT * FROM doctorVisit WHERE patient = '{id}'")
    records = cursor.fetchall()
    return records