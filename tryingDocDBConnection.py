import pymongo
from pymongo import MongoClient, errors

def connect_to_documentdb():
    try:
        # Replace the placeholders with your actual values
        endpoint = "translationdb.cluster-c782i6gi4sct.ap-south-1.docdb.amazonaws.com"
        port = 27017
        username = "translationdb"
        password = "admin123"

        # Construct the connection string
        uri = f"mongodb://{username}:{password}@{endpoint}:{port}/"

        # Connect to DocumentDB
        client = MongoClient(uri)
        print('printing dbs')
        print(client.list_database_names())
        print("printed")
        db = client.test_database  # Use any desired database

        return db
    except errors.ConnectionFailure as e:
        print(f"Error connecting to DocumentDB: {e}")
        return None

def insert_data(db):
    try:
        # Get a reference to the collection
        collection = db.test_collection

        # Insert a document
        result = collection.insert_one({"name": "John", "age": 30})

        print("Data inserted successfully.")
        return result.inserted_id
    except errors.PyMongoError as e:
        print(f"Error inserting data: {e}")
        return None

def get_data(db, inserted_id):
    try:
        # Get a reference to the collection
        collection = db.test_collection

        # Find the document by its ID
        document = collection.find_one({"_id": inserted_id})

        print("Data retrieved successfully:")
        print(document)
    except errors.PyMongoError as e:
        print(f"Error retrieving data: {e}")

# Connect to DocumentDB
db = connect_to_documentdb()

# Insert data
inserted_id = insert_data(db)

# Get data
if inserted_id:
    get_data(db, inserted_id)

