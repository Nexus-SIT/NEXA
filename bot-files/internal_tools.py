import requests

def websearch(query):
    url = "https://google-search74.p.rapidapi.com/"
    querystring = {"query":query,"limit":"3","related_keywords":"true"}
    headers = {
        "x-rapidapi-key": "0f74f2e409msh0b29a2c79506d6bp1383b8jsn595e259130b4",
        "x-rapidapi-host": "google-search74.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def play_music():
  print("Play music")
tools = [
{
      "type":"function",
      "function":{
          "name":"websearch",
          "description":"Search the top 4 results from google",
          "parameters":{
            "type": "object",
            "properties": {
              "query": {
                "type": "string",
                "description": "The search query to use for the web search."
              }
            },
            "required": ["query"]
          }
      }
  }
]

TOOL_MAPPING = {
    "websearch": websearch
}

