import streamlit as st
import fetchId
from langchain.llms import Bedrock
import boto3
from botocore.config import Config
import json
from langchain import PromptTemplate
import os
#import fetchTranslations

config = Config(read_timeout=1000)
bedrock_client = boto3.client(
    service_name='bedrock-runtime', 
    region_name='us-east-1',
    config=config
)
def interactWithLLM(prompt):
    # Prepend "Human:" to the prompt
    # prompt = "Human: " + prompt
    # # Append "Assistant:" to the prompt
    # prompt += "\nAssistant:"
    # "top_k":250,
    # "top_p":0.999,
    model_id = 'ai21.j2-ultra-v1'
    content_type = 'application/json'
    accept = 'application/json'
    max_tokens = 8000
    temperature = 0.9

    body = json.dumps({
            "prompt": prompt,
            "maxTokens": max_tokens,
            "temperature": temperature
        })

    response = bedrock_client.invoke_model(body=body, modelId=model_id, accept=accept, contentType=content_type)
    response_body = json.loads(response.get('body').read())

    response_text_claud = response_body.get('completions')[0].get('text')
    #print(response_body)
    return response_text_claud

#llm = Bedrock(credentials_profile_name="default",model_id="ai21.j2-ultra-v1",model_kwargs={"maxTokens":1000})

# Title for the app
st.title("Language Translation Tool")

# Dropdown for selecting the source language
source_language = st.selectbox(
    "Source Language",
    ('en-us', 'en-au', 'es-ar', 'de-de', 'fr-fr'),
    index=0,  # Default selection (en-us)
    key='source_language'  # Unique key for the widget
)

# Dropdown for selecting the target language
target_language = st.selectbox(
    "Target Language",
    ('en-us', 'en-au', 'es-ar', 'de-de', 'fr-fr'),
    index=1,  # Default selection (en-au)
    key='target_language'  # Unique key for the widget
)

# Large text area for XML input
xml_input = st.text_area("XML", height=300, key='xml_input')

# You can add a button to process the input
if st.button('Translate'):
    
    data=[]
    # Placeholder for processing logic
    st.write("Processing translation...")  # Example output
    # Here you can add the code to handle the translation process
    # and display the results or any other information.

# Displaying the selected options and input for demonstration purposes
    st.write("Source Language:", source_language)
    st.write("Target Language:", target_language)

    # Process the XML input and display the JSON output
    doc_id = fetchId.fetch_id(xml_input)
    #doc_id = 'CGI-C_PD_Psychosis'
    #translations = fetchTranslations.fetch_documents(doc_id, source_language, target_language)
    source_language = '''[ "Protocol",
        "Site Number",
        "Screening Number",
        "Randomization Number",
        "Assessment Date",
        "Rater",
        "Signature History",
        "Completed and Signed by",
        "Name",
        "Date/Time (UTC)",
        "Edited and Signed by",
        "Version",
        "Page2",
        "Page3",
        "Page4",
        "Page5",
        "Page6",
        "Considering your total clinical experience with the Parkinson's Disease population, how ill is this patient with respect to: \n&nbsp;",
        "Text1",
        "Normal (no symptoms present)",
        "Very mild",
        "Motor signs \n&nbsp;",
        "Motor signs",
        "Mild",
        "Mild to moderate",
        "Moderate",
        "Severe",
        "Very severe",
        "Normal (no symptoms present)",
        "Very mild",
        "Motor complications (dyskinesia and fluctuations) \n&nbsp;",
        "Motor complications",
        "Mild",
        "Mild to moderate",
        "Moderate",
        "Severe",
        "Very severe",
        "Normal (no symptoms present)",
        "Slowness and/or minimal cognitive problems",
        "Cognitive status \n&nbsp;",
        "Cognitive status",
        "Mild cognitive problems; no limitations",
        "Mild to moderate cognitive problems; does not need help for basic activities of daily living",
        "Moderate cognitive problems; help is required for some basic activities of daily living",
        "Severe cognitive problems; help is required for most or all basic activities of daily living",
        "Severely disabled; helpless; complete assistance needed",
        "Normal (no symptoms present)",
        "Minimal slowness and/or clumsiness",
        "Disability \n&nbsp;",
        "Disability",
        "Slowness and/or clumsiness; no limitations",
        "Limitation for demanding activities; does not need help for basic activities of daily living",
        "Limitation to perform basic activities of daily living; help is required for some basic daily living activities",
        "Great limitation to perform basic activities of daily living; help is required for most or all basic activities of daily living",
        "Severely disabled; helpless; complete assistance needed",
        "Notes"]'''
    target_language = '''[ "Protocolo",
        "Número de centro",
        "Número de selección",
        "Número de aleatorización",
        "Fecha de evaluación",
        "Evaluador",
        "Historial de firmas",
        "Completado y firmado por",
        "Nombre",
        "Fecha/hora (UTC)",
        "Editado y firmado por",
        "Versión",
        "Page2",
        "Page3",
        "Page4",
        "Page5",
        "Page6",
        "Teniendo en cuenta su experiencia clínica total con la población con enfermedad de Parkinson, ¿qué grado de enfermedad presenta este paciente con respecto a: \n&nbsp;",
        "Text1",
        "Normal (no presenta síntomas)",
        "Muy leve",
        "Signos motores \n&nbsp;",
        "Signos motores",
        "Leve",
        "De leve a moderado",
        "Moderado",
        "Grave",
        "Muy grave",
        "Normal (no presenta síntomas)",
        "Muy leve",
        "Complicaciones motoras (disquinesia y fluctuaciones) \n&nbsp;",
        "Complicaciones motoras (disquinesia y fluctuaciones)",
        "Leve",
        "De leve a moderado",
        "Moderado",
        "Grave",
        "Muy grave",
        "Normal (no presenta síntomas)",
        "Lentitud y/o problemas cognitivos mínimos",
        "Estado cognitivo \n&nbsp;",
        "Estado cognitivo",
        "Problemas cognitivos leves; sin limitaciones",
        "Problemas cognitivos de leves a moderados; no necesita ayuda para actividades básicas de la vida diaria",
        "Problemas cognitivos moderados; necesita ayuda para algunas actividades básicas de la vida diaria",
        "Problemas cognitivos graves; necesita ayuda para la mayoría o todas las actividades básicas de la vida diaria",
        "Discapacidad grave; no puede valerse por sí mismo; necesita asistencia completa",
        "Normal (no presenta síntomas)",
        "Lentitud o torpeza mínimas",
        "Discapacidad \n&nbsp;",
        "Discapacidad",
        "Lentitud o torpeza; sin limitaciones",
        "Limitaciones para actividades exigentes; no necesita ayuda para actividades básicas de la vida diaria",
        "Limitaciones para llevar a cabo actividades básicas de la vida diaria; necesita ayuda para algunas actividades básicas de la vida diaria",
        "Grandes limitaciones para llevar a cabo actividades básicas de la vida diaria; necesita ayuda para la mayoría o todas las actividades básicas de la vida diaria",
        "Discapacidad grave; no puede valerse por sí mismo; necesita asistencia completa",
        "Notas"]'''
    translations = {'source_lang': source_language, 'target_lang': target_language}
    st.write("extracted texts", translations)
    prompt = f"Based on a previous translation of an XML, from English(US) to Spanish (US), I have provided a JSON mapping as follows: \n {source_language} \n\nThe translation JSON mapping is: \n {target_language} \n\n Please provide the translation (in XML format) of the following XML in Spanish(US) language based on the given JSON mappings: \n{xml_input}"
    print(prompt)
    st.write(interactWithLLM(prompt))

# ls=[]
# if responses:
#     st.write("extracted texts", responses[0][0])
