from .data import *
class Dataprocess:

    def __init__(self, data):
        self.__data = data

    def create_careers(self, db, DATA):
        ## Do something to create careers on your mongodb collection using __data
        collection = db["Careers"]
        for index in DATA:
            campo = index['carrera']
            collection.update_one({'carrera':campo},
            {'$set':index},upsert=True)
        return True

    def create_courses(self, db, DATA):
        ## Do something to create courses on your mongodb collection using __data

        collection = db['Courses']
        for index in DATA:
            for valor in index['cursos_aprobados']:
                if not collection.find_one({'course': valor}):
                    collection.insert_one({'course': valor})

        return True
    def create_students(self, db, DATA):
        ## Do something to create students on your mongodb collection using __data
        collection = db["Students"]
        collection.insert_many(DATA)
        return True

    # def create_enrollments(self):
    #     ## Do something to create enrollments on your mongodb collection using __data
    #     print("\n\tStudents per Career\n")
    #     collection = db['Students']
    #     result = collection.aggregate([
    #       {  
    #         "$lookup": {
    #           "from": "Courses",
    #           "localField": "cursos_aprobados",
    #           "foreignField": "Course",
    #           "as": "courses_aprobados" },
    #           {
    #           "$project":{"_id":0,"nombre_completo":1,"cursos_aprobados":1}    
    #           }
    #       } 
    #     ])

    @staticmethod
    def get_students_per_career(db):
        print("\n\tStudents per Career\n")
        collection = db['Students']
        result = collection.aggregate([
            {"$group":{"_id":{"carrera":"$carrera"},"total":{"$sum":1}}}
        ])
        for i in result:
            print(i)

    @staticmethod
    def approved_by_course(db):
        print("\n\tStudents approved by courses\n")
        collection = db['Students']
        result = collection.aggregate([
            {"$unwind":"$cursos_aprobados"},
            {"$group":{"_id":{"Course":"$cursos_aprobados"},"Approved by course":{"$sum":1}}},
        ])
        for i in result:
            print(i)

    @staticmethod
    def failed_by_course(db):
        print("\n\tStudents failed by courses\n")
        collection = db['Students']
        result = collection.aggregate([
            {"$unwind":"$cursos_aprobados"},
            {"$group":{"_id":{"Course":"$cursos_aprobados"},"failed by course":{"$sum":1}}},
        ])
        for i in result:
            print(i)