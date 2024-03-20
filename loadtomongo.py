import os
import json
import re

def read_json_files(directory):
    json_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                print(file)
                json_files.append(os.path.join(root, file))

    json_data = []
    for file in json_files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            json_data.append(data)

    return json_data

# Usage example
directory_path = 'C:/Users/jaipreet.singh/Downloads/Forms/'
json_data = read_json_files(directory_path)
dump_data = {}
for data in json_data:
    match = re.search(r'([A-Za-z]{2}-[A-Za-z]{2})', str(data.keys()))
    if match:
        lang = match.group(1).lower()
        print(lang)    
    
    match = re.search(r'(.*\.)', str(list(data.keys())[0]))
    if match:
        id = match.group(1)
        texts = id.split('_')
        if len(texts) > 3:
            id = ' '.join(texts[:len(texts)-2]).lower()
            print(id)
            
        else:
            id = texts[0].lower() 
            print(id)
    if dump_data.get(id):
        dump_data[id].update({lang : list(data.values())[0]})
    else:
        dump_data[id] = {lang : list(data.values())[0]}
# print(dump_data['cgi-c hd alt1'].keys() )         

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['translations_db']
collection = db['translations']

# Insert data into the collection
for key, value in dump_data.items():
    document = {'_id': key, 'data': value}
    collection.insert_one(document)

# Close the connection
client.close()