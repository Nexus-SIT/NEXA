import requests
from openai import OpenAI
import json # Import the json module

universal_ai_key="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"

client = OpenAI(
base_url="https://openrouter.ai/api/v1",
api_key=universal_ai_key,)


def summerize_response(text_content): 

    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="meta-llama/llama-3.3-8b-instruct:free",
    messages=[
        {
            "role":"system","content":"Summerize the contents and just provide short reqired info on raw text"
        },
        {
        "role": "user",
        "content": text_content # Use the renamed parameter
        }
    ]
    )
    result=(completion.choices[0].message.content)
    return result

def google_search(query):
    url = "https://google-search72.p.rapidapi.com/search"

    querystring = {"q":query,"lr":"en-US","num":"2"}

    headers = {
        "x-rapidapi-key": "0f74f2e409msh0b29a2c79506d6bp1383b8jsn595e259130b4",
        "x-rapidapi-host": "google-search72.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    
google_search("Latest news of world today")