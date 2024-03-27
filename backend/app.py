from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient('mongodb://database:27017/')
db = client['mydatabase']
collection = db['users']

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    # Insert data into MongoDB
    collection.insert_one({'name': name, 'email': email})
    
    return jsonify({'message': 'Data submitted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
