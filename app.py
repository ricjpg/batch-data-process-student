import pymongo
from classes import DATA, Dataprocess, DbMongo, Students, Careers, Courses, data
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()

    #-------------------Cleanup------------------------#
    Students.delete_all(db)
    # Careers.delete_all(db)
    # Courses.delete_all(db)
    
    # pipeline = Dataprocess(db)

    # pipeline.create_careers()
    # pipeline.create_students()
    # pipeline.create_enrollments()

    #-------------------Setting some data------------------------#

    # Students("1221", "asdasd", "poo", "poo", "3", "IS").save(db)
    # Careers("IS").save(db)
    # Courses([data.DATA[1]]).save(db)
    
    # Dataprocess.create_careers(db)

    # Students.insert_many(data.DATA)
    # for s in data.DATA:
    #     Students(DATA).save(db)
    
    # Students(data.DATA[0]).save(db)
    
    # Students().save(db)
    # Students(DATA).saveAll(db, DATA)
    # Students(DATA[2]).save(db)
    # Students(db).savver(db)

    Students(DATA[0]['numero_cuenta'],
            DATA[0]['nombre_completo'],
            DATA[0]['cursos_aprobados'],
            DATA[0]['cursos_reprobados'],
            DATA[0]['edad'],
            DATA[0]['carrera'],
            ).save(db)
    Students(DATA[1]['numero_cuenta'],
            DATA[1]['nombre_completo'],
            DATA[1]['cursos_aprobados'],
            DATA[1]['cursos_reprobados'],
            DATA[1]['edad'],
            DATA[1]['carrera'],
            ).save(db)



    return True
    client.close()

if __name__ == "__main__":
    load_dotenv()
    main()
