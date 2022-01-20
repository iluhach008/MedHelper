from . import cursor


def getAll():
    cursor.execute('SELECT id as "value", name FROM level')
    records = cursor.fetchall()
    return records


def getByID(id):
    cursor.execute(f'SELECT id, name FROM level WHERE id = {id}')
    records = cursor.fetchone()
    if records:
        return records
    return None