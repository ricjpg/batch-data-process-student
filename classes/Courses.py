

class Courses:

    def __init__(self, courses, id = ""):
        self.courses = courses
        self.__id = id
        self.__collection = "Courses"


    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

    def update(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )

    @staticmethod
    def save_all_DATA(db,DATA):
        collection = db['Courses']
        # for dicc in DATA:
        #     campoA = dicc['cursos_aprobados']
        #     # campoR = dicc['cursos_reprobados']
        #     collection.update_one({'cursos_aprobados':campoA},
        #     {'$set':dicc},upsert=True)
        #     # collection.update_one({'cursos_reprobados':campoR},
        #     # {'$set':dicc},upsert=True)
        cursos = []
        for dic in DATA:
            for cursos_aprobados in dic['cursos_aprobados']:
                cursos.append(cursos_aprobados)

        cursos = list(set(cursos))
        for cursos_aprobados in cursos:
            collection.insert_one({'cursos_aprobados': cursos_aprobados})


    @staticmethod
    def get_list(db):
        collection = db["Courses"]
        courses = collection.find()

        list_c = []
        for s in courses:
            temp_c = Courses(
                s["cursos_aprobados"],
                s["_id"]
                )
            list_c.append(temp_c)
        return list_c

    @staticmethod
    def delete_all(db):
        list_c = Courses.get_list(db)
        for c in list_c:
            c.delete(db)

