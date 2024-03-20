import streamlit as st
import fetchId
import fetchTranslations
import sendPrompt

# Title for the app
st.title("Language Translation Tool")

# Dropdown for selecting the source language
source_language = st.selectbox(
    "Source Language",
    ('en-us', 'en-au', 'es-us', 'de-de', 'fr-fr','fr-ca'),
    index=0,  # Default selection (en-us)
    key='source_language'  # Unique key for the widget
)

# Dropdown for selecting the target language
target_language = st.selectbox(
    "Target Language",
    ('en-us', 'en-au', 'es-us', 'de-de', 'fr-fr', 'fr-ca'),
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
    source,target = fetchTranslations.fetch_documents(doc_id, source_language, target_language)
    if source and target:
        translations = {source_language: source, target_language: target}
        prompt = f"{translations} \n  strictly follow the above translation mapping pattern of languages provided, Please translate the following XML from {source_language} to {target_language} language based on the given JSON mappings: \n{xml_input} and provide the output in the same XML format"
    else:
        prompt= f"Please translate the following XML from {source_language} to {target_language} language - \n{xml_input} and provide the output in the same XML format"
    
    print(prompt)
    
    response = sendPrompt.interactWithLLM(prompt)
    print (response)
    st.write("extracted texts", response)
    

# ls=[]
# if responses:
#     st.write("extracted texts", responses[0][0])
