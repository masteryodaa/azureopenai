import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") 
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_version = "2024-02-01"

response = openai.ChatCompletion.create(
    engine="gpt35", # engine = "deployment_name".
    messages=[
        {"role": "system", "content": "You are an AI Translation Assistant. If the input text is in English you will translate it in Hindi with context remaining the same. And if the input text is in Hindi you will have to translate it in English with context remaining the same."},
        # {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        # {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        # {"role": "user", "content": "Do other Azure AI services support this too?"}
        {"role": "user", "content": "Oh, please make sure he remains hydrated. Have you seen skin rash around his buttocks area?"}
    ]
)

# print(response)
print(response['choices'][0]['message']['content'])


