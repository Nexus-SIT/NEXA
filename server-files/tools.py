import requests

def get_weather(api_key="", latitude="40.730610", longitude="-73.935242"):
    """
    Fetches current weather data from OpenWeatherMap API.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": "metric"  # You can change to "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
    return response.json()
