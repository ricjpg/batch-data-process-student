import pymongo
from classes import DATA, Dataprocess, DbMongo, Students, Careers, Courses, data
from dotenv import load_dotenv
import pprint

def main():
    printer = pprint.PrettyPrinter()
    client, db = DbMongo.getDB()
    pipeline = Dataprocess(DATA)

    #--------------------Cleanup------------------------#
    #---------drop every collection to start fresh------#
    
    db.Students.drop()
    db.Careers.drop()
    db.Enrollments.drop()
    db.Courses.drop()

    #----------Setting all the data in the collections----------#


    pipeline.create_careers(db,DATA)
    pipeline.create_students(db,DATA)
    pipeline.create_courses(db,DATA)
    pipeline.create_enrollments(db,DATA)


    #-----------------Retrieve some data-----------------------#
    #----------------------------REPORTS-----------------------#
    
    Careers.get_students_per_career(db)
    Courses.get_approved(db)
    Courses.get_failed(db)
    
    

    # return True
    client.close()

if __name__ == "__main__":
    load_dotenv()
    main()
