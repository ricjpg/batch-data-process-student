from .data import *
class Students:

    def __init__(self, numero_cuenta, nombre_completo, cursos_aprobados, cursos_reprobados, edad, carrera, id = ""):
        self.numero_cuenta = numero_cuenta
        self.nombre_completo = nombre_completo
        self.cursos_aprobados = cursos_aprobados
        self.cursos_reprobados = cursos_reprobados
        self.edad = edad
        self.carrera = carrera
        self.__id = id
        self.__collection = "Students"
    

    #este es el bueno
    # def __init__(self, objStudent, id = ""):
    #     self.objStudent = objStudent
    #     self.__id = id
    #     self.__collection = "Students"

    # numero_cuenta = data.Data(numero_cuenta)
    # nombre_completo = data.Data(nombre_completo)
    # cursos_aprobados = data[data.Data(cursos_aprobados)]
    # cursos_reprobados = data.Data(cursos_reprobados)
    # edad = data.Data(edad)
    # carrera = data.Data(carrera)

    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id = result.inserted_id



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
    def get_list(db):
        collection = db["Students"]
        student = collection.find()
        list_student = []
        for s in student:
            temp_student = Students(
                s["numero_cuenta"],
                s["nombre_completo"],
                s["cursos_aprobados"],
                s["cursos_reprobados"],
                s["edad"],
                s["carrera"],
                s["_id"]
                )
            list_student.append(temp_student)
        return list_student

    @staticmethod
    def save_all_DATA(db, DATA):
        for index in DATA:
            Students(index['numero_cuenta'],
                index['nombre_completo'],
                index['cursos_aprobados'],
                index['cursos_reprobados'],
                index['edad'],
                index['carrera'],
                ).save(db)

    @staticmethod
    def delete_all(db):
        list_s = Students.get_list(db)
        for s in list_s:
            s.delete(db)


    @staticmethod
    def get_list_careers(db):
        collection = db["Students"]
        student = collection.find()
        list_student = []
        for s in student:
            temp_student = Students(
                s["numero_cuenta"],
                s["nombre_completo"],
                s["cursos_aprobados"],
                s["cursos_reprobados"],
                s["edad"],
                s["carrera"],
                s["_id"]
                )
            list_student.append(temp_student)
            return list_student['carrera']

    

    # @staticmethod
    # def get_just_careers(db):
    #     collection = db["Students"]
    #     result = collection.aggregate([
    #         {'$group':{'_id':'$carrera'}},
    #         {'$count':'carrera'},
    #         {
    #             '$project': {
    #                 '_id': 0,
    #                 'carrera': 1,
    #         }
    #         }
    #     ])
    #     for e in result:
    #         print(e)

    # @staticmethod
    # def get_just_careers(db):
    #     collection = db["Students"]
    #     result = collection.aggregate([
    #         {'$lookup':{'from':''}},
    #         {'$count':'carrera'},
    #         {
    #             '$project': {
    #                 '_id': 0,
    #                 'carrera': 1,
    #         }
    #         }
    #     ])
    #     for e in result:
    #         print(e)

    @staticmethod
    def get_just_careers(db):
        collection = db["Students"]
        result = collection.aggregate([
            {"$group":{"_id":{"carrera":"$carrera"}}}
        ])
        for e in result:
            print(e)

    @staticmethod
    def get_just_courses(db):
        collection = db["Students"]
        result = collection.aggregate([
            {"$unwind":"$cursos_aprobados"},
            {"$group":{"_id":{"Course":"$cursos_aprobados"}}},

        ])
        for e in result:
            print(e)