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
        print(client)
        db = client.jp_db  # Use any desired database
        col = db.jp
        col.insert_one({"Jp":"Test"})
        print(db.list_collection_names())
        # Print the list of databases to verify the connection
        print(client.list_database_names())

        return db
    except errors.ConnectionFailure as e:
        print(f"Error connecting to DocumentDB: {e}")
        return None

# Connect to DocumentDB
db = connect_to_documentdb()

print("Hello")
