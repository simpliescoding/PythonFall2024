from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/', methods=['GET'])    
def home():
    return 'HOME'

# Move the MongoDB connection outside of the route functions
client = MongoClient('mongodb+srv://Chhay:123123321@cluster0.hvdl2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client["LASALLFALL2024"]
users_collection = db["Users"]

print(users_collection)



@app.route('/users', methods=['GET'])
def get_users():
    users = []
    for user in users_collection.find():
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
        users.append(user)  # Add the user to the list correctly
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True)
