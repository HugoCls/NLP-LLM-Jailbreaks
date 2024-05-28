from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

MISTRAL_API_KEY = os.getenv('mistral_api_key')

client = MistralClient(api_key=MISTRAL_API_KEY)

def response(prompt, model="mistral-large-latest"):

    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=prompt)]
    )

    message = chat_response.choices[0].message.content

    final_message = f"{datetime.datetime.now()}::{model}::{message}".replace('\n', ' ')

    with open(f"results/Mistral.txt", "a", encoding="utf-8") as f:
        f.write(f"{final_message}\n")
    
    return final_message