# api/weather.py
"""
Weather API integration for fetching weather information.
"""
import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join('config', 'config.env'))

class WeatherAPI:
    def __init__(self):
        self.api_key = os.getenv("WEATHER_API_KEY", "")
        self.base_url = "http://api.openweathermap.org/data/2.5"
    
    def get_weather(self, city):
        """
        Get current weather for a city.
        
        Args:
            city (str): City name
        """
        if not self.api_key:
            return "Weather API key not configured. Please add WEATHER_API_KEY to config.env"
        
        endpoint = f"{self.base_url}/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            
            return (f"Weather in {city}: {description}. "
                   f"Temperature is {temp}°C, feels like {feels_like}°C. "
                   f"Humidity is {humidity}%.")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                return f"City '{city}' not found."
            return f"Error fetching weather: {str(e)}"
        except Exception as e:
            return f"Error fetching weather: {str(e)}"
    
    def get_forecast(self, city, days=3):
        """Get weather forecast for a city."""
        if not self.api_key:
            return "Weather API key not configured."
        
        endpoint = f"{self.base_url}/forecast"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "cnt": days * 8  # 8 forecasts per day (3-hour intervals)
        }
        
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            forecasts = []
            for item in data["list"][::8][:days]:  # One per day
                date = item["dt_txt"].split()[0]
                temp = item["main"]["temp"]
                description = item["weather"][0]["description"]
                forecasts.append(f"{date}: {description}, {temp}°C")
            
            return f"Forecast for {city}: " + ". ".join(forecasts)
        except Exception as e:
            return f"Error fetching forecast: {str(e)}"
