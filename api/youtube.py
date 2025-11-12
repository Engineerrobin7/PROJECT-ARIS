# api/youtube.py
"""
YouTube API integration for searching and playing videos.
"""
import requests
import webbrowser
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join('config', 'config.env'))

class YouTubeAPI:
    def __init__(self):
        self.api_key = os.getenv("YOUTUBE_API_KEY", "")
        self.base_url = "https://www.googleapis.com/youtube/v3"
    
    def search_video(self, query):
        """
        Search for a YouTube video and return the top result.
        
        Args:
            query (str): Search query
        """
        if not self.api_key:
            # Fallback to direct search without API
            search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            webbrowser.open(search_url)
            return f"Opening YouTube search for '{query}'."
        
        endpoint = f"{self.base_url}/search"
        params = {
            "part": "snippet",
            "q": query,
            "type": "video",
            "maxResults": 1,
            "key": self.api_key
        }
        
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if "items" in data and len(data["items"]) > 0:
                video_id = data["items"][0]["id"]["videoId"]
                video_title = data["items"][0]["snippet"]["title"]
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                
                webbrowser.open(video_url)
                return f"Playing '{video_title}' on YouTube."
            else:
                return f"No videos found for '{query}'."
        except Exception as e:
            # Fallback to direct search
            search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            webbrowser.open(search_url)
            return f"Opening YouTube search for '{query}'."
    
    def play_video(self, query):
        """Alias for search_video."""
        return self.search_video(query)
