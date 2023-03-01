from classes.DbMongo import DbMongo
from .data import *

class Courses:

    def __init__(self, courses, id = ""):
        self.courses = courses
        self.__id = id
        self.__collection = "Courses"


    @staticmethod
    def get_approved(db):
        print("\n\tStudents approved by courses\n")
        collection = db['Students']
        result = collection.aggregate([
            {"$unwind":"$cursos_aprobados"},
            {"$group":{"_id":{"Course":"$cursos_aprobados"},"Approved":{"$sum":1}}},
        ])
        for i in result:
            print(i)

    @staticmethod
    def get_failed(db):
        print("\n\tStudents failed by courses\n")
        collection = db['Students']
        result = collection.aggregate([
            {"$unwind":"$cursos_reprobados"},
            {"$group":{"_id":{"Course":"$cursos_reprobados"},"Failed":{"$sum":1}}}
        ])
        for i in result:
            print(i)


#################################################################################

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
