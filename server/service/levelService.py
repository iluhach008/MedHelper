from dal import levelDal


def getAll():
    return levelDal.getAll()


def getByID(id):
    return levelDal.getByID(id)