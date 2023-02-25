import pymongo
from classes import DATA, Dataprocess, DbMongo, Students, Careers, Courses
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()

    #-------------------Cleanup------------------------#
    Students.delete_all(db)
    Careers.delete_all(db)
    Courses.delete_all(db)

    # pipeline = Dataprocess(db)

    # pipeline.create_careers()
    # pipeline.create_students()
    # pipeline.create_enrollments()

    # Students("data.numero_cuenta", 
    #         "data.nombre_completo", 
    #         "data.cursos_aprobados", 
    #         "data.cursos_reprobados", 
    #         "data.edad", "data.carrera").save(db)
    #-------------------Setting some data------------------------#
    
    Students("1221", "asdasd", "poo", "poo", "3", "IS").save(db)
    Careers("IS").save(db)
    Courses("OOP").save(db)


    return True
    client.close()

if __name__ == "__main__":
    load_dotenv()
    main()
