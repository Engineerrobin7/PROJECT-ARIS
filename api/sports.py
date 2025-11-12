# api/sports.py
"""
Sports API integration for fetching scores and schedules.
"""
import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join('config', 'config.env'))

class SportsAPI:
    def __init__(self):
        self.api_key = os.getenv("SPORTS_API_KEY", "")
        self.base_url = "https://api.the-odds-api.com/v4"
    
    def get_scores(self, sport="basketball_nba"):
        """
        Get recent scores for a sport.
        
        Args:
            sport (str): Sport key (e.g., 'basketball_nba', 'soccer_epl')
        """
        if not self.api_key:
            return "Sports API key not configured. Please add SPORTS_API_KEY to config.env"
        
        endpoint = f"{self.base_url}/sports/{sport}/scores"
        params = {
            "apiKey": self.api_key,
            "daysFrom": 1
        }
        
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if not data:
                return f"No recent scores found for {sport}."
            
            scores = []
            for game in data[:5]:
                home = game.get("home_team", "Unknown")
                away = game.get("away_team", "Unknown")
                scores.append(f"{away} vs {home}")
            
            return "Recent games: " + ", ".join(scores)
        except Exception as e:
            return f"Error fetching sports scores: {str(e)}"
