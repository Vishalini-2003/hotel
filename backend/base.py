from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Welcome to Flask App!'

@app.route('/add-user', methods=['POST','GET'])
def add_user():
    data = request.get_json()
    username = data['name']
    password = data['password']
    email = data['email']

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1981_2003v",
        database="hotel"
    )

    cursor = db.cursor()

    query = "INSERT INTO login (username, password, email) VALUES (%s, %s, %s)"
    values = (username, password, email)

    cursor.execute(query, values)

    db.commit()

    return jsonify({'message': 'User created successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)