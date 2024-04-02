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


