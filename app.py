import pymongo
from classes import DATA, Dataprocess, DbMongo
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()
    
    # pipeline = Dataprocess(DATA)
    
    # pipeline.create_careers()
    # pipeline.create_students()
    # pipeline.create_enrollments()

    # return True
    client.close()

if __name__ == "__main__":
    load_dotenv()
    main()
