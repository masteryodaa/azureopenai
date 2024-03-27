import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Replace these variables with your actual values
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
deployment_name = "speech"

url = f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{deployment_name}/audio/speech?api-version=2024-02-15-preview"

headers = {
    "api-key": AZURE_OPENAI_API_KEY,
    "Content-Type": "application/json"
}

data = {
    "model": "tts-hd",
    "input": "Oh, please make sure he remains hydrated. Have you seen skin rash around his buttocks area?",
    "voice": "alloy" # alloy, echo, fable, onyx, nova, and shimmer
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    with open("speech.mp3", "wb") as f:
        f.write(response.content)
        print("Audio file saved successfully.")
else:
    print(f"Failed to generate audio: {response.status_code} - {response.text}")


# textToSpeechWithTranslation
# speechToSpeechWithTranslation