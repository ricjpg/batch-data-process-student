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
    Courses.delete_all(db)


    #-------------------idk----------------------------#
    # pipeline = Dataprocess(db)

    # pipeline.create_careers()
    # pipeline.create_students()
    # pipeline.create_enrollments()


    #-------------------Setting some data------------------------#
    # Careers.save_all_DATA(db,DATA)
    # Students.save_all_DATA(db,DATA)
    # Courses.save_all_DATA(db,DATA)
    # Careers.quantity(db)
    # Careers.save_all_DATA(db,Students.get_list_careers)
    # Careers.quantity(db)
    # Students.quantity(db)

    Courses.save_all_DATA(db,DATA)

    #-------------------Retrieving data------------------------#
    # print(Courses.get_courses_approved(db))


    # return True
    client.close()

if __name__ == "__main__":
    load_dotenv()
    main()
