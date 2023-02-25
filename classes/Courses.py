

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
    def get_list(db):
        collection = db["Courses"]
        courses = collection.find()

        list_courses = []
        for s in courses:
            temp_courses = Courses(
                s["courses"],
                s["_id"]
                )
            list_courses.append(temp_courses)
        return list_courses


    @staticmethod
    def delete_all(db):
        list_c = Courses.get_list(db)
        for c in list_c:
            c.delete(db)