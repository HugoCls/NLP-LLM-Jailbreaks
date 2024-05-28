#pip install -q -U google-generativeai (requirement)

import google.generativeai as genai
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

GEMINI_API_KEY = os.getenv('gemini_api_key')

def response(prompt, model="gemini-1.5-flash"):

    genai.configure(api_key=GEMINI_API_KEY)

    model = genai.GenerativeModel(model)

    message = model.generate_content(prompt).text

    final_message = f"{datetime.datetime.now()}::{model}::{message}".replace('\n', ' ')

    with open(f"results/Gemini.txt", "a", encoding="utf-8") as f:
        f.write(f"{final_message}\n")

    return message