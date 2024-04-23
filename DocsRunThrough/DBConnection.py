import pymysql

#double check your information is correct for each of these variables
def connectToDB():
    dbName = "IoT" 
    user="sictc"
    password="Pencil1"
    host="localhost"

    #connection is your db connection object
    connection = pymysql.connect(
        database = dbName,
        user=user,
        password=password,
        host=host
    )

    try:
        #if the connection is good
        if connection:
            print("\nConnected to the db\n")
            #return connection
    #py.ysql.Error is a built in module that creates error reports for you based on the feedback from the db
    except pymysql.Error as e:
        print(f"Error connecting to db: {e}")
        #return None
    
connectToDB()
