import requests
from Music import search_and_play

def websearch(query):
    url = "https://google-search74.p.rapidapi.com/"
    querystring = {"query":query,"limit":"3","related_keywords":"true"}
    headers = {
        "x-rapidapi-key": "0f74f2e409msh0b29a2c79506d6bp1383b8jsn595e259130b4",
        "x-rapidapi-host": "google-search74.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


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
  },{
      "type":"function",
      "function":{
          "name":"search_and_play",
          "description":"Searches for a song (e.g., on YouTube Music) and plays it.",
          "parameters":{
            "type": "object",
            "properties": {
              "song_name": {
                "type": "string",
                "description": "The name of the song to search for and play. Including the artist can improve results."
              }
            },
            "required": ["song_name"]
          }
      }
  }
]

TOOL_MAPPING = {
    "websearch": websearch,
    "search_and_play":search_and_play
}

