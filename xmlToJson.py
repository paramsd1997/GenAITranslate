# from google.colab import drive
import xml.etree.ElementTree as ET
import os
import json
import bleach


# Remount Google Drive
#drive.mount("/content/drive", force_remount=True)


# Specify the allowed tags for bleach (empty list means all tags will be stripped)
allowed_tags = []

data=[]

def extract_text(element):
    """Recursively extracts text from the XML tree."""
    if element.text:
        # Remove extra spaces and newlines
        text = ' '.join(element.text.strip().split())
        if text:
            # Use bleach to clean HTML and CSS tags
            cleaned_text = bleach.clean(text, tags=allowed_tags, strip=True)
            data.append(cleaned_text)
    for child in element:
        extract_text(child)

def process_xml_string(xml_str):
        print(xml_str)
        try:
            tree = ET.ElementTree(ET.fromstring(xml_str))
            root = tree.getroot()
            extract_text(root)
            # Convert data to JSON without escaping UTF-8 characters
            data_list = json.dumps(data, indent=4, ensure_ascii=False)
            data.clear()
            # print(data_list)
            return data_list.replace('[','').replace(']','')
            # return ','.join(data)
        
        except ET.ParseError:
            print(f"XML parsing error for xml. Please check if the XML string is well-formed.")
            return None

print(process_xml_string('''<?xml version="1.0" encoding="UTF-8"?>
<form id="4faeebf8-f404-47a5-b13b-688d2dcafc9e" abbreviation="CGI-C" version="1.0" build="9" culture="Español (US)" cultureid="es-US" timestamp="2021-10-22T08:39:04.330Z"><item id="8b9e09f6-40ca-4a60-b455-a32cb5755097">Protocolo</item><item id="61f2da8a-4ad8-4a38-9273-d87b5088076b">Número de centro</item><item id="be6d4bcf-f7b8-49d8-b448-ed6de3271744">Número de selección</item><item id="83fae26b-5c38-4901-8f16-3562de824c0c">Número de aleatorización</item><item id="233319fc-bbd9-402d-9d0d-7e3fc8848876">Fecha de evaluación</item><item id="c397f3ab-638a-46ec-b56b-59dcd0f519d8">Evaluador</item><item id="79c020a5-1e5d-4ffc-aed9-3dae45e20270">Historial de firmas</item><item id="3ec5b441-0595-4cb2-bea6-a2cc88ee3a3a">Completado y firmado por</item><item id="24ee5be4-25c4-41cd-8919-328c118921c8">Nombre</item><item id="9b88ea09-c625-4322-88d6-790fbee54ff2">Fecha/Hora (UTC)</item><item id="be8b0a22-b99b-440c-be1d-07f1e8203f89">Editado y firmado por</item><item id="917d7db1-8e97-44ff-a72a-9f5af1fc6ddc">Versión</item><item id="c37e5b4c-c631-4313-9201-e7b6d6fb544e@c4f2159a-dc75-4e3a-8af1-57056cd78e89">Page2</item><item id="36b2c704-5772-446a-96b9-fee5fda94d70@4dcfbe32-295f-43d7-9e31-364ad3447af4">Page7</item><item id="39f7e3be-8d88-4d23-9cd1-ff735979f1fd@e307357c-536e-4aa8-9854-8498c4c73dd2">&lt;div style="text-align: left;"&gt;&amp;nbsp;&lt;/div&gt; &lt;div style="text-align: left;"&gt;En comparación con la condición basal del paciente, ¿cuánto ha cambiado la psicosis relacionada con la enfermedad de Parkinson del sujeto con respecto a las alucinaciones y delirios?&lt;/div&gt; &lt;div style="text-align: left;"&gt;Califique el cambio total, independientemente de si, en su opinión, se debe enteramente al tratamiento.&lt;/div&gt;</item><item id="39f7e3be-8d88-4d23-9cd1-ff735979f1fd@11ada9c4-b2c9-4894-b203-32c958307371">Text1</item><item id="2201202d-6670-4ffd-8cf1-3e56d014f0c3@44878037-13f9-4f7d-bacf-e2f7d2b612e3">&lt;p&gt;Muy mejorado&lt;/p&gt;</item><item id="2201202d-6670-4ffd-8cf1-3e56d014f0c3@2bd98d72-3ef1-4d32-b867-b5dc26b3497d">&lt;p&gt;Mucho mejor&lt;/p&gt;</item><item id="2201202d-6670-4ffd-8cf1-3e56d014f0c3@74f7aa08-6bba-416e-a8b8-be12ffb0bbfc">&lt;div style="text-align: left;"&gt; &lt;div style="text-align: left;"&gt;En comparación con la condición basal del paciente, ¿cuánto ha cambiado la psicosis relacionada con la enfermedad de Parkinson del sujeto con respecto a las alucinaciones y delirios?&lt;/div&gt; &lt;div style="text-align: left;"&gt;Califique el cambio total, independientemente de si, en su opinión, se debe enteramente al tratamiento.&lt;/div&gt; &lt;/div&gt;</item><item id="2201202d-6670-4ffd-8cf1-3e56d014f0c3@2fb2364d-04d4-44c3-8f6c-f186bd0f289a">CGI-C PD Psychosis</item><item id="2201202d-6670-4ffd-8cf1-3e56d014f0c3@62b51f19-f216-4cf1-b0f7-4b704ffca8a6">&lt;p&gt;Mínimamente mejorado&lt;/p&gt;</item><item id="2201202d-6670-4ffd-8cf1-3e56d014f0c3@0bc0edc6-7fb1-4662-8e18-f58379714a5c">&lt;p&gt;Sin cambios&lt;/p&gt;</item><item id="2201202d-6670-4ffd-8cf1-3e56d014f0c3@d1c98fa9-dfa1-4ada-a372-3162d55819d3">&lt;p&gt;Mínimamente peor&lt;/p&gt;</item><item id="2201202d-6670-4ffd-8cf1-3e56d014f0c3@318ae313-e04c-4795-a0d8-1bd683fd2281">&lt;p&gt;Mucho peor&lt;/p&gt;</item><item id="2201202d-6670-4ffd-8cf1-3e56d014f0c3@40d3841d-a27e-4140-aad2-c048d6146063">&lt;p&gt;Muy empeorado&lt;/p&gt;</item><item id="19d85030-b756-4968-bd40-9e466ba2761b@ca709238-c285-42c2-8dae-05dd5cef49b1">Notas</item></form>'''))
# Specify the main directory path in Google Drive
#main_directory_path = '/content/drive/MyDrive/GenAI_Translation_Platform'


# Process XML files in the main directory and its subdirectories
#process_xml_files(main_directory_path)


