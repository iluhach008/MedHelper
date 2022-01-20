from . import cursor, conn


def getAll():
    cursor.execute('SELECT e.id, e.name, e.surname, e.fathername, e.login, e.address, e.phone, '
                   'l.name as level FROM employee as e JOIN level as l ON e.level = l.id')
    records = cursor.fetchall()
    return records


def getAllBySpecialization(id):
    cursor.execute(f'SELECT e.id, e.name, e.surname, e.fathername FROM employee as e WHERE e.specialization = {id}')
    records = cursor.fetchall()
    return records


def getByID(id):
    cursor.execute(f'SELECT * FROM employee WHERE id = {id}')
    records = cursor.fetchone()
    return records




def getIdByLogin(login):
    cursor.execute(f"SELECT id FROM employee WHERE login = '{login}'")
    records = cursor.fetchone()
    return records


def getByLoginPassword(login, password):
    cursor.execute(f"SELECT e.id, e.name, e.surname, e.fathername, e.login, l.name as level "
                   f"FROM employee as e JOIN level as l ON e.level = l.id "
                   f"WHERE login = '{login}' and password ='{password}' ")
    records = cursor.fetchone()
    return records


def register(data):
    cursor.execute(f"INSERT INTO employee "
                   f"(address, education, fathername, gender, level, login, name, "
                   f"password, phone, surname, specialization, creator, created) VALUES "
                   f"('{data['address']}', '{data['education']}', '{data['fathername']}', '{data['gender']}', "
                   f"{data['level']},'{data['login']}', '{data['name']}', '{data['password1']}', '{data['phone']}', "
                   f"'{data['surname']}', {data['specialization']}, {data['creator']}, '{data['created']}') RETURNING id")
    records = cursor.fetchone()
    conn.commit()
    return records['id']


def update(id, data):
    cursor.execute(f"UPDATE employee SET "
                   f"address ='{data['address']}', "
                   f"education ='{data['education']}', "
                   f"fathername ='{data['fathername']}', "
                   f"gender ='{data['gender']}', "
                   f"level ={data['level']}, "
                   f"login ='{data['login']}', "
                   f"name ='{data['name']}', "
                   f"password ='{data['password1']}', "
                   f"phone ='{data['phone']}', "
                   f"surname ='{data['surname']}', "
                   f"specialization ={data['specialization']}, "
                   f"creator ={data['creator']}, "
                   f"created = '{data['created']}' "
                   f"WHERE id = {id} RETURNING id")
    records = cursor.fetchone()
    conn.commit()
    return records['id']


def deleteByID(id):
    cursor.execute(f'DELETE FROM employee WHERE id = {id}')
    conn.commit()
    return True
