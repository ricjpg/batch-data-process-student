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
    def saveAll(self, data, db):
        collection = db[self.__collection]
        student = collection.find()
        list_st = []
        for s in student:
            list_st.append(data[s])
        return list_st


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

    #este va con solo objStudent
    # @staticmethod
    # def get_list(db):
    #     collection = db["Students"]
    #     student = collection.find()

    #     list_student = []
    #     for s in student:
    #         temp_student = Students(
    #             s["objStudent"],
    #             s["_id"]
    #             )
    #         list_student.append(temp_student)
    #     return list_student


    @staticmethod
    def delete_all(db):
        list_s = Students.get_list(db)
        for s in list_s:
            s.delete(db)

    @staticmethod
    def insert_many(db):
        collection = db["Students"]
        for s in students:
            collection.insert_one(s.__dict__)