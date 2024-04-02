import xmlToJson

from langchain.vectorstores import Chroma
from langchain.embeddings import BedrockEmbeddings

def fetch_id(xml_input):
    # print(xml_input)
    xml_json = xmlToJson.process_xml_string(xml_input)
    
    print('*'*20)
    # print(xml_json)
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
    responses = db.similarity_search_with_score(xml_json, k=1)
    # print(responses)
    return responses[0][0].metadata['id']

# print(fetch_id(''' "Protocolo",
#         "Número de centro",
#         "Número de selección",
#         "Número de aleatorización",
#         "Fecha de evaluación",
#         "Evaluador",
#         "Historial de firmas",
#         "Completado y firmado por",
#         "Nombre",
#         "Fecha/hora (UTC)",
#         "Editado y firmado por",
#         "Versión",
#         "Página2",
#         "Página3",
#         "Gravedad de la capacidad para funcionar",
#         "Pautas",
#         "&nbsp; \nDe las respuestas a continuación, seleccione la que mejor describa la gravedad en la capacidad del sujeto para funcionar a causa del temblor esencial durante la última semana (7 días). \n&nbsp;",
#         "Ninguna limitación",
#         "Leve&nbsp;",
#         "Moderada&nbsp;",
#         "Marcada",
#         "Significativa",
#         "SingleChoice1",
#         "Notas"'''))
