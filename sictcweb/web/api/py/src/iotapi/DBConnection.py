import pymysql
from dotenv import load_dotenv

#Loading the .env file into memory
load_dotenv()

def connectToDB():   #???could put in optional parameters???
    dbName = "IoT"              # os.getenv("dbName")#"IoT"
    user = "sictc"               #os.getenv("dbUser")#"root"
    password = "Pencil1"      #os.getenv("password")#"Password1"
    host = "localhost"          #os.getenv("host")#'localhost'
                                # print(dbName,user,password,host)

    connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=dbName
        )
    try:
        if connection:
            print("Connected to the database")
            return connection
    except pymysql.Error as e:
        print(f"Error connecting to db: {e}")
        return None

connectToDB()