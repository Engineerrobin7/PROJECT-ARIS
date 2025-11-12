# api/news.py
"""
News API integration for fetching latest news headlines.
"""
import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join('config', 'config.env'))

class NewsAPI:
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY", "")
        self.base_url = "https://newsapi.org/v2"
    
    def get_top_headlines(self, country="us", category=None, query=None):
        """
        Fetch top headlines from News API.
        
        Args:
            country (str): Country code (e.g., 'us', 'gb')
            category (str): Category (business, entertainment, health, science, sports, technology)
            query (str): Search query
        """
        if not self.api_key:
            return "News API key not configured. Please add NEWS_API_KEY to config.env"
        
        endpoint = f"{self.base_url}/top-headlines"
        params = {
            "apiKey": self.api_key,
            "country": country,
            "pageSize": 5
        }
        
        if category:
            params["category"] = category
        if query:
            params["q"] = query
        
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data.get("status") == "ok":
                articles = data.get("articles", [])
                if not articles:
                    return "No news articles found."
                
                headlines = []
                for i, article in enumerate(articles[:5], 1):
                    title = article.get("title", "No title")
                    headlines.append(f"{i}. {title}")
                
                return "Here are the top headlines: " + ". ".join(headlines)
            else:
                return "Failed to fetch news."
        except Exception as e:
            return f"Error fetching news: {str(e)}"
    
    def search_news(self, query):
        """Search for news articles by query."""
        if not self.api_key:
            return "News API key not configured."
        
        endpoint = f"{self.base_url}/everything"
        params = {
            "apiKey": self.api_key,
            "q": query,
            "pageSize": 5,
            "sortBy": "publishedAt"
        }
        
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data.get("status") == "ok":
                articles = data.get("articles", [])
                if not articles:
                    return f"No news found for '{query}'."
                
                headlines = []
                for i, article in enumerate(articles[:5], 1):
                    title = article.get("title", "No title")
                    headlines.append(f"{i}. {title}")
                
                return f"News about {query}: " + ". ".join(headlines)
            else:
                return "Failed to search news."
        except Exception as e:
            return f"Error searching news: {str(e)}"
