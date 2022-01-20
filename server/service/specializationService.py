from dal import specializationDal


def getAll():
    return specializationDal.getAll()


def getAllSimple():
    return specializationDal.getAllSimple()


def getIdByName(name):
    return specializationDal.getIdByName(name)


def getNameByID(id):
    return specializationDal.getNameByID(id)


def create(name):
    return specializationDal.create(name)


def getOrCreate(name):
    id = getIdByName(name)
    if not id:
        id = create(name)
    return id