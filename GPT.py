from openai import OpenAI
from dotenv import load_dotenv
import os
import glob
import pandas as pd
import logging as log

load_dotenv()

OPENAI_API_KEY = os.getenv('openai_api_key')

client = OpenAI(api_key=OPENAI_API_KEY)

pricing = {
    "gpt-3.5-turbo-0125": {
        "input":0.5,
        "output":1.5,
    },
    "gpt-3.5-turbo-instruct": {
        "input":1.5,
        "output":2,
    },
    "gpt-3.5-turbo": {
        "input":3,
        "output":6,
    },
}


def query(context, model="gpt-3.5-turbo"):
    
    log.info(f"Query: {context} w/ Model: {model}")
    response = client.chat.completions.create(
        model=model,
        messages=context,
    )

    completion_tokens = response.usage.completion_tokens
    prompt_tokens = response.usage.prompt_tokens
    input_price = pricing[model]["input"] * prompt_tokens / 1000000
    output_price = pricing[model]["output"] * completion_tokens / 1000000

    output = response.choices[0].message.content

    return output, completion_tokens, prompt_tokens, input_price, output_price
      

if __name__ == "__main__":
    model = "gpt-3.5-turbo-0125"

    context = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "This is a test"}
    ]

    message, completion_tokens, prompt_tokens, input_price, output_price = query(context=context, model=model)
    
    final_message = f"{model}:{completion_tokens}:{prompt_tokens}:{input_price}:{output_price}:{message}"
    
    with open(f"data/GPT_results.txt", "a", encoding="utf-8") as f:
        f.write(final_message)