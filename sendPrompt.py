from langchain.llms import Bedrock
import boto3
from botocore.config import Config
import json

config = Config(read_timeout=1000)
bedrock_client = boto3.client(
    service_name='bedrock-runtime', 
    region_name='us-east-1',
    config=config)

def interactWithLLM(prompt):
    # Prepend "Human:" to the prompt
    prompt = "Human: " + prompt
    # Append "Assistant:" to the prompt
    prompt += "\nAssistant:"
    # "top_k":250,
    # "top_p":0.999,
    model_id = 'anthropic.claude-v2:1'
    content_type = 'application/json'
    accept = 'application/json'
    max_tokens =16000
    temperature = 0.9

    body = json.dumps({
            "prompt": prompt,
            "max_tokens_to_sample": max_tokens,
            "temperature": temperature
        })

    response = bedrock_client.invoke_model(body=body, modelId=model_id, accept=accept, contentType=content_type)
    response_body = json.loads(response.get('body').read())
    print(response_body)

    response_text_claud = response_body.get('completion')
    #print(response_body)
    return response_text_claud