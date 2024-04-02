from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import json
import re
# import argparse
# from dotenv import load_dotenv
# from langchain.chains import RetrievalQA
#from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import BedrockEmbeddings
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
# from langchain.vectorstores.azuresearch import AzureSearch
from langchain.vectorstores import Chroma
from langchain.schema.document import Document
from langchain.document_loaders.json_loader import JSONLoader
from langchain.document_loaders.xml import UnstructuredXMLLoader

# import json

from chromadb.config import Settings
# Define the folder for storing database
# embeddings = HuggingFaceEmbeddings(model_name='all-mpnet-base-v2')
embeddings = BedrockEmbeddings(credentials_profile_name="default",model_id="cohere.embed-multilingual-v3")
# # Define the Chroma settings
CHROMA_SETTINGS = Settings(
        chroma_db_impl='duckdb+parquet',
        persist_directory='db',
        anonymized_telemetry=False
)
db = Chroma(
        persist_directory='db',
        embedding_function=embeddings,
        client_settings=CHROMA_SETTINGS,
    )





def read_json_files(directory):
    json_files = []
    for root, dir, files in os.walk(directory):
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
directory_path = 'C:/Users/parmeshwar.1/Desktop/Ukraine_genAI/All_EN_Json'
json_data = read_json_files(directory_path)
dump_data = {}
for data in json_data:
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

        text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=2000,
                chunk_overlap=0,
                length_function=len
                )
        text=",".join(list(data.values())[0])
        chunks = text_splitter.split_text(text=text)
        for chunk in chunks:

                data = [Document(page_content = chunk , metadata= {'id':id}  )]
                print(type(data))
                db.add_documents(data)



