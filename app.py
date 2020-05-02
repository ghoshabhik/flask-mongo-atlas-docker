import os
import json

from flask import Flask, redirect, request, jsonify, Response
from pymongo import MongoClient
#from bson.json_util import dumps

app =Flask(__name__)


client = MongoClient("mongodb+srv://avik5324:avik5324@abhikatlasmumbaiin-16jmi.mongodb.net/test?retryWrites=true&w=majority")

db = client.tododb

@app.route('/')
def todo():
    return "This is Todo Atlas DB"

@app.route('/get/<id>', methods=['GET'])
def getTodo(id):
    todo = db.todo.find_one({"my_id": id})
    print(todo)
    responseTodo = {'Id': todo['my_id'], 'name': todo['name'], 'description': todo['description']}
    return jsonify({"results":responseTodo})

@app.route('/get', methods=['GET'])
def getAllTodo():
    todos = []
    for todo in db.todo.find():
        todos.append({'Id': todo['my_id'], 'name': todo['name'], 'description': todo['description']})
        print(todo)
    return jsonify({'results': todos})

@app.route('/add', methods=['POST'])
def addTodo():
    newTodo = request.json
    print(newTodo['name'])
    db.todo.insert_one(newTodo)
    return jsonify({"msg":'Added'})


if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
