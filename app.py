import pymongo
from classes import DATA, Dataprocess, DbMongo, Students, Careers, Courses, data
from dotenv import load_dotenv
import pprint

def main():
    printer = pprint.PrettyPrinter()
    client, db = DbMongo.getDB()
    #-------------------Cleanup------------------------#
    # Students.delete_all(db)
    # Careers.delete_all(db)
    # Courses.delete_all(db)


    #----------I didnt use this functions--------------#

    #----------########-UPDATE-###########--------------#
    #----------Now i can use this funtions--------------#
    #---------drop every collection to start fresh------#
    
    db.Students.drop()
    db.Careers.drop()
    db.Courses.drop()
    pipeline = Dataprocess(DATA)

    # #------------Set all the data in collection----------#


    pipeline.create_careers(db,DATA)
    pipeline.create_students(db,DATA)
    pipeline.create_courses(db, DATA)

    #-----------------Retrieve some data----------------#
    pipeline.get_students_per_career(db)
    pipeline.approved_by_course(db)
    pipeline.failed_by_course(db)
    # pipeline.get_enrollements(db)
    # pipeline.create_enrollments()


    #-------------------Setting some data------------------------#
    # Careers.save_all_DATA(db,DATA)
    # Students.save_all_DATA(db,DATA)
    # Courses.save_all_DATA(db,DATA)


    # #-------------------Retrieving data------------------------#
    # #this method the number of students in every career
    # Students.get_just_careers(db) 
    # print("----------------------------------------------------------------")
    
    
    # #this method shows the number of students approved by course
    # Students.approved_by_course(db) 
    # print("----------------------------------------------------------------")
    

    # #this method shows the number of students failed by course
    # Students.failed_by_course(db)

    # return True
    client.close()

if __name__ == "__main__":
    load_dotenv()
    main()
