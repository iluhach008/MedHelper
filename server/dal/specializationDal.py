from . import cursor, conn


def getAll():
    cursor.execute("SELECT name as value, name FROM specialization")
    records = cursor.fetchall()
    return records


def getAllSimple():
    cursor.execute("SELECT * FROM specialization")
    records = cursor.fetchall()
    return records


def getIdByName(name):
    cursor.execute(f"SELECT id FROM specialization WHERE name = '{name}'")
    records = cursor.fetchone()
    if records:
        return records['id']
    return None


def getNameByID(id):
    cursor.execute(f"SELECT name FROM specialization WHERE id = '{id}'")
    records = cursor.fetchone()
    if records:
        return records['name']
    return None


def create(name):
    cursor.execute(f"INSERT INTO specialization (name) VALUES ('{name}') RETURNING id")
    records = cursor.fetchone()
    conn.commit()
    return records['id']