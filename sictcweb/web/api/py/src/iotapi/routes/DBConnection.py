import pymysql

def connectToDB():   #???could put in optional parameters???
        dbName = "IoT"              # os.getenv("dbName")#"IoT"
        user = "root"               #os.getenv("dbUser")#"root"
        password = "Password1"      #os.getenv("password")#"Password1"
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
    