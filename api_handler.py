# api_handler.py
import requests
from config import WEATHER_API_KEY, NEWS_API_KEY

def get_weather(city):
    """Fetches the current weather data for a specified city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for bad status codes (4xx or 5xx)
        data = response.json()
        
        if data.get("cod") != 200:
            return None, data.get("message", "Unknown error")

        weather_info = {
            "description": data['weather'][0]['description'],
            "temperature": data['main']['temp'],
            "city": data['name']
        }
        return weather_info, None
    except requests.exceptions.RequestException as e:
        return None, str(e)
    except KeyError:
        return None, "Unexpected API response format for weather data."


def get_news(country_code='gb'):
    """Fetches the top news headlines for a specified country."""
    url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data.get("status") != "ok":
            return None, data.get("message", "Unknown error")
            
        # Get the top 3 articles
        articles = data.get("articles", [])[:3]
        headlines = [article['title'] for article in articles]
        return headlines, None
    except requests.exceptions.RequestException as e:
        return None, str(e)
    except KeyError:
        return None, "Unexpected API response format for news data."
