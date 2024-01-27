from flask import Flask, request, redirect, url_for, jsonify, Blueprint, send_file, render_template
import pymysql
from dotenv import load_dotenv
import json

#create application object to hadnle the different routes
stateBP = Blueprint('stateBP',__name__)

#Loading the .env file into memory
load_dotenv()

#put all of the db connection material in separate class
import sys                  #GPT this, needed to put the eonnection stuff in separate file
sys.path.append('routes/')  
from DBConnection import connectToDB
#Typically this would be with the imports, but here for learning
connection=connectToDB()

@stateBP.route('/welcome')
def statePage():
    allData=getAll()
    print(f'\n\nwelcome route: {allData}\n\n')
    '''????????????????????????????????????????????????????????????????????????????
        allData is currently just the response code and data but need to convert it.
            Ok need to figure this one out...  The API is sending jsonify data, but
                Jinja doesn't take the response straight. It needs to be converted 
                back to a dictionary or hashmap thing?
    ????????????????????????????????????????????????????????????????????????????'''
    return render_template('States/States.html',data=allData)

#GET/READ everyrecord from Accounts Table
@stateBP.route('/')
def getAll():
    queryString = f"SELECT * FROM States"
    try:
        out=""
        with connection.cursor() as cursor:
            cursor.execute(queryString)
            rows = cursor.fetchall()
            # print(type(rows))
            # print(rows)
            sorted_data_byId = sorted(rows,key=lambda x: x[0])   #chatGPT this code
            userJsonData=[]
            for row in sorted_data_byId:
                data={
                        'id':row[0],
                        'state':row[1]
                        }
                userJsonData.append(data)
            print('userJsonData: ',userJsonData)
            createFile(userJsonData,'Data/test.txt')
    except pymysql.Error as e:
        print(f"Error connecting to db: {e}")
    except:
        return "oops something went wrong"
    #return jsonify(userJsonData)
    return userJsonData

#GET 1 record from Accounts Table
@stateBP.route('/id/<id>')
def getById(id):
    queryString=f'SELECT * FROM States WHERE Id = {id}'
    print(queryString)

    try:
        out=""
        with connection.cursor() as cursor:
            cursor.execute(queryString)
            rows = cursor.fetchone()        ###fetchone() cuz only 1 item
            print(rows)
            userJsonData=[]                 ###convert rows to json
            data={
                  'id':rows[0],
                  'state':rows[1]
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
@stateBP.route('/add',methods=['POST'])
def addIt():
    if request.is_json:
        data = request.get_json()
        state = data.get("State")
    else:
        data_from_form = request.form['input_data']
        # print(data_from_form)
        state = data_from_form

    queryString=f'INSERT INTO States (State) VALUES ("{state}")'
    print(queryString)
    try:
        with connection.cursor() as cursor:
            cursor.execute(queryString)
        connection.commit()                 #saves the request to the db
    except pymysql.Error as e:
        print(f"Error connecting to db: {e}")
    except:
        return "oops something went wrong"
    return redirect(url_for('stateBP.statePage'))   #for some reason with the Jinja the stateBP is required
    #got an error somewhere...  the id is jumping by 2?   Need to verify this error

#DELETE 1 record from States Table
@stateBP.route('/delete',methods=['POST'])#'DELETE'])
def deleteIt():
    if request.is_json:
        data = request.get_json()
        id = data.get("Id")
    else:
        data_from_form = request.form['input_data']
        # print(data_from_form)
        id = data_from_form
    
    queryString=f'DELETE FROM States WHERE Id = {id}'
    print(queryString)
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(queryString)
        connection.commit()                 #saves the request to the db
    except pymysql.Error as e:
        print(f"Error connecting to db: {e}")
    except:
        return "\noops something went wrong"
    
    return redirect(url_for('stateBP.statePage'))
    #https://medium.com/@carlospineda/why-no-methods-for-put-delete-in-html-f483b66d8874
    #https://softwareengineering.stackexchange.com/questions/114156/why-are-there-no-put-and-delete-methods-on-html-forms

#UPDATE 1 record from Accounts Table
@stateBP.route('/update',methods=['POST'])
def updateIt():
    if request.is_json:
        data = request.get_json()
        id = data.get("Id")
        state = data.get("State")
    else:
        id = request.form.get('idData')
        state = request.form.get('stateData')
        print(id,state)
        #Each input field has a unique name attribute (name="name", name="age", name="city"), which is used to identify the data when the form is submitted.
        #The for attribute of the <label> elements is associated with the id attribute of the corresponding input field. This improves accessibility and usability.

    queryString=f"UPDATE States SET State='{state}' WHERE Id={id}"
    print(f"\n{queryString}\n")
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(queryString)
            connection.commit()
    except pymysql.Error as e:
        print(f"Error connecting to db: {e}")
    except:
        return "oops something went wrong"
    # return redirect(url_for('getAll'))
    return redirect(url_for('stateBP.statePage'))

#download CSV file of the current DB
#TODO:  still need to finish. This will only send the file, could we 
#           get this to run the / route and createFile and download?
@stateBP.route('/download')
def downloadAll():
    filename='Data/test.txt'
    return send_file(filename,as_attachment=True)   #NEED the as_attachment for the browsers to understand this link has a file

def createFile(data, filePath):
    with open(filePath, 'w') as file:
        json.dump(data, file)  #.dump() takes the object and makes it a string to be written
    print(f'Data has been written to {filePath}')

@stateBP.route('/JinjaAdd')
def addState():
    #even with this in the templates folder and this in a blueprint, app.py needs the template directory in its app.py's cwd
    return render_template('/States/States.html')

#since the template was rendered here, app.py knows to go look for this route
@stateBP.route('/process_data', methods=['POST'])
def process_data():
    # Get the JSON data from the form
    data_from_form = request.form['input_data']
    # print(data_from_form)
    # Process the data as needed
    processed_data = {'result': f'You entered: {data_from_form}'}

    # Return the processed data as JSON
    return jsonify(processed_data)
