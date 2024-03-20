from pymongo import MongoClient

def fetch_documents(id,source_lang, target_lang):
    # Create a client connection to your MongoDB instance
    client = MongoClient('mongodb://localhost:27017/')

    # Access the 'translations_db' database
    db = client['translations_db']

    # Access the 'translations' collection
    collection = db['translations']
    id = " ".join(id.split('_')).lower()
    # Perform a query to fetch all documents
    documents = collection.find_one({'_id' : id})
    print(id)
    print(documents)

    # Print each document
    print(documents['data'].keys())
    source = documents['data'].get(source_lang)
    target = documents['data'].get(target_lang)
    print(source)
    print(target)
    return source, target
    

# Call the function
# fetch_documents('cgi-c hd alt1' , 'en-ca', 'es-ar')