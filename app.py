# app.py

# Import the Flask module
from flask import Flask , render_template
from flask import jsonify


# Import the PyMongo module to interact with MongoDB
from pymongo import MongoClient

# Create a Flask application instance
app = Flask(__name__)

# Connect to the MongoDB container
# We use the hostname "mongodb" to connect to the MongoDB container
# as it will be automatically resolved to the IP address of the container
# within the Docker network
client = MongoClient("mongodb://mongodb:27017/")

# Get a reference to the test_database
#db = client.test_database
 
# Get a reference to the test_collection
db = client.personne

# Get a reference to the test_collection
collection = db.poste

# Define the route for the index page
@app.route("/")
def index():
    # Fetch a single document from the test_collection
    data = [
    {key: str(value) if key == "_id" else value for key, value in d.items()}
    for d in collection.find()
]
    # Return the fetched data as a string
    return jsonify(data)


@app.route('/text')
def get_text():
    with open('/app/data/text.txt', 'r') as file:
        file_contents = file.read()
    return jsonify(file_contents)

# Start the Flask application if this file is being executed as the main script
if __name__ == "__main__":
    # Start the Flask application, listening on all available interfaces
    app.run(host="0.0.0.0")
