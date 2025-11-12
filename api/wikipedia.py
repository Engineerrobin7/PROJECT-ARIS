# api/wikipedia.py
"""
Wikipedia API integration for fetching article summaries.
"""
import requests

class WikipediaAPI:
    def __init__(self):
        self.base_url = "https://en.wikipedia.org/api/rest_v1"
    
    def search(self, query):
        """
        Search Wikipedia and return a summary.
        
        Args:
            query (str): Search query
        """
        # First, search for the article
        search_url = "https://en.wikipedia.org/w/api.php"
        search_params = {
            "action": "opensearch",
            "search": query,
            "limit": 1,
            "format": "json"
        }
        
        try:
            response = requests.get(search_url, params=search_params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if len(data) > 1 and len(data[1]) > 0:
                title = data[1][0]
                return self.get_summary(title)
            else:
                return f"No Wikipedia article found for '{query}'."
        except Exception as e:
            return f"Error searching Wikipedia: {str(e)}"
    
    def get_summary(self, title):
        """Get summary of a Wikipedia article by title."""
        endpoint = f"{self.base_url}/page/summary/{title}"
        
        try:
            response = requests.get(endpoint, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            extract = data.get("extract", "")
            if extract:
                # Limit to first 2 sentences for brevity
                sentences = extract.split(". ")
                summary = ". ".join(sentences[:2]) + "."
                return summary
            else:
                return f"No summary available for '{title}'."
        except Exception as e:
            return f"Error fetching Wikipedia summary: {str(e)}"
