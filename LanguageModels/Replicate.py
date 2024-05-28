
from replicate.client import Client
from replicate.pagination import async_paginate as _async_paginate
from replicate.pagination import paginate as _paginate
from dotenv import load_dotenv
import os
import datetime
    
load_dotenv()

REPLICATE_API_KEY = os.getenv('replicate_api_key')

client = Client(api_token=REPLICATE_API_KEY)


def response(prompt, model="mistral-large-latest"):

    message = client.run(
        "meta/meta-llama-guard-2-8b:b063023ee937f28e922982abdbf97b041ffe34ad3b35a53d33e1d74bb19b36c4",
        input=prompt
    )

    final_message = f"{datetime.datetime.now()}::{model}::{message}".replace('\n', ' ')

    with open(f"results/Replicate.txt", "a", encoding="utf-8") as f:
        f.write(f"{final_message}\n")

    return final_message