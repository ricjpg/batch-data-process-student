from .data import *
class Dataprocess:

    def __init__(self, data):
        self.__data = data

    def create_careers(self, db, DATA):
        # Do something to create careers on your mongodb collection using __data
        collection = db["Careers"]

        for index in DATA:
            campo = index['carrera']
            collection.update_one(
                {'carrera':campo},
                {'$set':{}},
                upsert=True
            )
        return True

    def create_students(self, db, DATA):
        ## Do something to create students on your mongodb collection using __data
        collection = db["Students"]
        collection.insert_many(DATA)
        return True



    def create_enrollments(self, db, DATA):
        collection = db['Students']
        collectionToEn = db['Enrollments']
        result = collection.aggregate([
            {
                "$lookup": {
                    "from": "Students",
                    "localField": "nombre_completo",
                    "foreignField": "cursos_aprobados",
                    "as": "enrollments" }
            },
            {
                '$project':{
                    "nombre_completo":1,
                    "cursos_aprobados":1
                }
            },
            {
                '$set':{"nombre_completo":"$nombre_completo"}
            }
        ])
        for e in result:
            collectionToEn.insert_one(e)
        return True


    def create_courses(self, db, DATA):
        ## Do something to create courses on your mongodb collection using __data
        collection = db['Courses']
        for index in DATA:
            for valor in index['cursos_aprobados']:
                if not collection.find_one({'course': valor}):
                    collection.insert_one({'course': valor})
        return True

