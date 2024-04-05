from flask import Flask, Blueprint, jsonify
import pymysql
from routes.DBConnection import connectToDB

connection = connectToDB()
accountBP = Blueprint('accountBP',__name__)

@accountBP.route('/welcome')
def hello():
    return "Hello and welcome to the Accounts route of the IoT API!"

#GET/READ everyrecord from Accounts Table
@accountBP.route('/')
def getAll():
    global connection
    print("slash route ran")
    queryString = f"SELECT * FROM Accounts"
    print("18: ",connection)
    try:
        with connection.cursor() as cursor:
            print(cursor)
            cursor.execute(queryString)
            rows = cursor.fetchall()
            # print(type(rows))
            # print(rows)
            sortedDataById = sorted(rows,key=lambda x: x[0])   #chatGPT this code
            userJsonData=[]
            for row in sortedDataById:
                data={
                        'Id':row[0],
                        'Name':row[1],
                        'Address':row[2],
                        'City':row[3],
                        'State':row[4],
                        'Zip':row[5]
                        }
                userJsonData.append(data)
            print('userJsonData: ',userJsonData)
            return jsonify(userJsonData)
    except pymysql.Error as e:
        print(f"Error connecting to db: {e}")
        return f"Error connecting to db: {e}"
    except:
        print("non-pymysql error")
        return "oops something went wrong"























































