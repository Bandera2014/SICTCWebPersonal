from flask import Flask, request, redirect, url_for, jsonify, Blueprint, send_file, make_response
import pymysql
from dotenv import load_dotenv
import sys
sys.path.append('../')
from DBConnection import connectToDB
connection=connectToDB()

#create application object to hadnle the different routes
accountBP = Blueprint('accountBP',__name__)
  
@accountBP.route('/welcome')
def hello():
    return "Hello and welcome to the Accounts route of the IoT API"

#GET/READ everyrecord from Accounts Table
@accountBP.route('/')
def getAll():
    print("slash route ran")
    queryString = f"SELECT * FROM Accounts"
    try:
        with connection.cursor() as cursor:
            cursor.execute(queryString)
            rows = cursor.fetchall()
            # print(type(rows))
            # print(rows)
            sorted_data_byId = sorted(rows,key=lambda x: x[0])   #chatGPT this code
            userJsonData=[]
            for row in sorted_data_byId:
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
    except pymysql.Error as e:
        print(f"Error connecting to db: {e}")
    except:
        return "oops something went wrong"

    return jsonify(userJsonData)
    #finally:                       ###  Should be used to stop db connection
        #connection.close()

#GET 1 record from Accounts Table
@accountBP.route('/<id>')
def getById(id):
    queryString=f'SELECT * FROM Accounts WHERE Id = {id}'
    print(queryString)

    try:
        with connection.cursor() as cursor:
            cursor.execute(queryString)
            rows = cursor.fetchone()        ###fetchone() cuz only 1 item
            print(rows)
            userJsonData=[]                 ###convert rows to json
            data={
                  'id':rows[0],
                  'Name':rows[1]
                  }
            userJsonData.append(data)
            print(userJsonData)
    except pymysql.Error as e:
        print(f"Error connecting to db: {e}")
    except:
        return "oops something went wrong"
    #finally:
    #    connection.close()
    
    return jsonify(userJsonData)

#ADD/POST/CREATE 1 record to Accounts Table
@accountBP.route('/add',methods=['POST'])
def addIt():
    if request.is_json:
        data = request.get_json()
        name = data.get("Name")
        address = data.get("Address")
        city = data.get("City")
        zipCode = data.get("Zip")
        state = data.get("State")
    else:
        state = "OH"
    queryString=f"INSERT INTO Accounts (Name, Address, City, Zip, State) VALUES ('{name}','{address}','{city}','{zipCode}','{state}')"
    # queryString=f'INSERT INTO Accounts (State) VALUES ("{state}")'
    print(queryString)
    try:
        with connection.cursor() as cursor:
            cursor.execute(queryString)
        connection.commit()                 #saves the request to the db
    except pymysql.Error as e:
        print(f"Error connecting to db: {e}")
    except:
        #utilizing this method will be great for Android and the API
        error_data = {
            'status': 'error',
            'message': str(e)
        }
        #utilizing this method will be great for Android and the API
        return jsonify(error_data), 500

    # return redirect(url_for('getAll'))
    response_data = {
            'status': 'success',
            'message': 'You have been registered successfully.'
        }
    return jsonify(response_data), 200

#DELETE 1 record from Accounts Table
@accountBP.route('/delete/<id>',methods=['DELETE'])
def deleteIt(id):
    '''if request.is_json:
        data = request.get_json()
        id = data.get("Id")
    else:
        return "no JSON data provided"
        id = 0'''
    queryString=f'DELETE FROM Accounts WHERE Id = {id}'
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(queryString)
        connection.commit()                 #saves the request to the db
    except pymysql.Error as e:
        print(f"Error connecting to db: {e}")
    except:
        return "oops something went wrong"
    return make_response('',200)
    #return redirect(url_for('getAll'))

#UPDATE 1 record from Accounts Table
@accountBP.route('/update',methods=['POST'])
def updateIt():
    if request.is_json:
        data = request.get_json()
        id = data.get("Id")
        name = data.get("Name")
        address = data.get("Address")
        city = data.get("City")
        state = data.get("State")
        zip = data.get("Zip")
    else:
        return "no JSON data provided"
        id = 9
        state = 'AK'
    queryString=f"UPDATE Accounts SET Name = '{name}', Address = '{address}', City = '{city}', State = '{state}', Zip = '{zip}' WHERE Id = {id}"
    print(queryString)
    try:
        with connection.cursor() as cursor:
            cursor.execute(queryString)
            connection.commit()
    except pymysql.Error as e:
        print(f"Error connecting to db: {e}")
    except:
        return "oops something went wrong"
    return make_response('',200)
    #return redirect(url_for('getAll'))

def queryThis(queryString):
    try:
        with connection.cursor() as cursor:
            cursor.execute(queryString)
            connection.commit()
            return True
    except pymysql.Error as e:
        return(False,f"Error connecting to db: {e}")
    except:
        return (False,"oops something went wrong")
'''#DELETE 1 record from Accounts Table
@accountBP.route('/delete',methods=['DELETE'])
def deleteIt():
    if request.is_json:
        data = request.get_json()
        id = data.get("Id")
    else:
        return "no JSON data provided"
        id = 0
    queryString=f'DELETE FROM Accounts WHERE Id = {id}'
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(queryString)
        connection.commit()                 #saves the request to the db
    except pymysql.Error as e:
        print(f"Error connecting to db: {e}")
    except:
        return "oops something went wrong"
   ''' 
