import openai
import time
import os

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = "azure"
openai.api_version = "2024-02-01"

model_name = "whisper"
deployment_id = "transcribe" #This will correspond to the custom name you chose for your deployment when you deployed a model."
audio_language="en"

audio_test_file = "./a.wav"

result = openai.Audio.transcribe(
            file=open(audio_test_file, "rb"),            
            model=model_name,
            deployment_id=deployment_id
        )

print(result.text)
