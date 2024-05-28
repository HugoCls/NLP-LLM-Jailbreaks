import google.generativeai as genai
from dotenv import load_dotenv
import os
import datetime
from google.generativeai.types import HarmCategory, HarmBlockThreshold

load_dotenv()

GEMINI_API_KEY = os.getenv('gemini_api_key')

def response(prompt, model_name="gemini-1.5-flash"):

    genai.configure(api_key=GEMINI_API_KEY)

    model = genai.GenerativeModel(model_name)

    message = model.generate_content(prompt, safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE}).text

    final_message = f"{datetime.datetime.now()}::{model_name}::{message}".replace('\n', ' ')

    with open(f"results/Gemini.txt", "a", encoding="utf-8") as f:
        f.write(f"{final_message}\n")

    return message