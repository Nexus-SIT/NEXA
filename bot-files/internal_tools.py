import requests

def search_gutenberg_books(search_terms):
    search_query = " ".join(search_terms)
    url = "https://gutendex.com/books"
    response = requests.get(url, params={"search": search_query})

    simplified_results = []
    for book in response.json().get("results", []):
        simplified_results.append({
            "id": book.get("id"),
            "title": book.get("title"),
            "authors": book.get("authors")
        })

    return simplified_results

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
    "type": "function",
    "function": {
      "name": "search_gutenberg_books",
      "description": "Search for books in the Project Gutenberg library based on specified search terms",
      "parameters": {
        "type": "object",
        "properties": {
          "search_terms": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of search terms to find books in the Gutenberg library (e.g. ['dickens', 'great'] to search for books by Dickens with 'great' in the title)"
          }
        },
        "required": ["search_terms"]
      }
    }
  },{
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
    "search_gutenberg_books": search_gutenberg_books,
    "websearch": websearch
}

