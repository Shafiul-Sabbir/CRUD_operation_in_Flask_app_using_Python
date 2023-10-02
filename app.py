""" My Cute API """
from flask import Flask, request
database = {'minhaj' : '100','sabbir' : '200'}

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return "welcome to my web API."

@app.route('/getdata/', methods = ['GET'])
def get_data():
    return database

@app.route('/adddata/', methods = ['GET','POST'])
def add_data():
    key, value = list(request.args.items())[0]
    database[key] = value
    return f"{key} added"

@app.route('/deletedata/', methods = ['GET','DELETE'])
def del_data():
    key, value = list(request.args.items())[0]
    database.pop(value)
    return f"{value} deleted"

@app.route('/updatedata/',methods = ['GET', 'PUT'])
def update_data():
    key,value = list(request.args.items())[0]
    if key in database:
        database[key]= value
        return f'{key} updated to {value}'
    else:
        return f'{key} not found in database'

if __name__ == '__main__':
    app.run()