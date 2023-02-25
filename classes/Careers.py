from classes.DbMongo import DbMongo
from .data import *
class Careers:
    
    def __init__(self, careers, id = ""):
        self.careers = careers
        self.__id = id
        self.__collection = "Careers"

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
    def get_list(db):
        collection = db["Careers"]
        career = collection.find()

        list_careers = []
        for s in career:
            temp_career = Careers(
                s["careers"],
                s["_id"]
                )
            list_careers.append(temp_career)
        return list_careers


    @staticmethod
    def delete_all(db):
        list_c = Careers.get_list(db)
        for c in list_c:
            c.delete(db)
