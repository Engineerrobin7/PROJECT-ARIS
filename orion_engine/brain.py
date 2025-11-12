# orion_engine/brain.py
"""
Core decision logic for ARIS. Routes commands to the appropriate modules.
"""
from commands import system_commands, web_commands, ai_commands, fun_commands
from commands import games_commands, multilang_commands, automation_commands
from api.weather import WeatherAPI
from api.news import NewsAPI
from api.wikipedia import WikipediaAPI
from api.youtube import YouTubeAPI
from api.stocks import StocksAPI
from api.sports import SportsAPI
from api.calendar_api import CalendarAPI
from api.email_api import EmailAPI
from orion_engine.nlp_module import NLPModule
from orion_engine.memory import Memory
from orion_engine.personality import Personality

class Brain:
    """The core logic unit of ARIS. It processes commands and delegates tasks."""
    def __init__(self):
        self.nlp = NLPModule()
        self.memory = Memory()
        self.personality = Personality()
        
        # Initialize API integrations
        self.weather_api = WeatherAPI()
        self.news_api = NewsAPI()
        self.wikipedia_api = WikipediaAPI()
        self.youtube_api = YouTubeAPI()
        self.stocks_api = StocksAPI()
        self.sports_api = SportsAPI()
        self.calendar_api = CalendarAPI()
        self.email_api = EmailAPI()
        
        print("Orion Engine Brain initialized with all integrations.")

    def route_command(self, command_text):
        """
        Analyzes the command text and routes it to the correct module.
        """
        if not command_text:
            return "I didn't catch that. Could you please repeat?"
            
        command_text = command_text.lower()
        print(f"Brain received command: '{command_text}'")
        
        # Add to memory
        self.memory.add_to_history(command_text)
        
        # Enhanced keyword-based routing with new features
        response = None
        
        # System commands
        if "open" in command_text or "start" in command_text or "run" in command_text or "close" in command_text:
            response = system_commands.handle_command(command_text)
        
        # Web commands
        elif "search" in command_text or "google" in command_text or "find" in command_text:
            response = web_commands.handle_command(command_text)
        
        # Weather commands
        elif "weather" in command_text or "temperature" in command_text or "forecast" in command_text:
            city = self._extract_city(command_text)
            if "forecast" in command_text:
                response = self.weather_api.get_forecast(city)
            else:
                response = self.weather_api.get_weather(city)
        
        # News commands
        elif "news" in command_text or "headlines" in command_text:
            if "about" in command_text:
                query = command_text.split("about")[-1].strip()
                response = self.news_api.search_news(query)
            else:
                response = self.news_api.get_top_headlines()
        
        # Wikipedia commands
        elif "wikipedia" in command_text or "wiki" in command_text:
            query = command_text.replace("wikipedia", "").replace("wiki", "").replace("search", "").strip()
            response = self.wikipedia_api.search(query)
        
        # YouTube commands
        elif "youtube" in command_text or "play video" in command_text or "play music" in command_text:
            query = command_text.replace("youtube", "").replace("play video", "").replace("play music", "").replace("play", "").strip()
            response = self.youtube_api.search_video(query)
        
        # Stock/Crypto commands
        elif "stock" in command_text or "stock price" in command_text:
            symbol = self._extract_symbol(command_text)
            response = self.stocks_api.get_stock_price(symbol)
        elif "crypto" in command_text or "bitcoin" in command_text or "ethereum" in command_text:
            symbol = self._extract_crypto_symbol(command_text)
            response = self.stocks_api.get_crypto_price(symbol)
        
        # Sports commands
        elif "sports" in command_text or "scores" in command_text or "game" in command_text:
            response = self.sports_api.get_scores()
        
        # Calendar commands
        elif "calendar" in command_text or "event" in command_text or "schedule" in command_text:
            if "add" in command_text or "create" in command_text:
                response = "Calendar event creation needs date and time. Please say: 'add event [title] on [date]'"
            else:
                response = self.calendar_api.get_events()
        
        # Email commands
        elif "email" in command_text or "mail" in command_text:
            if "check" in command_text or "unread" in command_text:
                response = self.email_api.check_unread_emails()
            else:
                response = "To send an email, please use the GUI or specify recipient and message."
        
        # Game commands
        elif any(word in command_text for word in ["game", "play", "coin", "dice", "8 ball", "trivia", "guess"]):
            response = games_commands.handle_command(command_text)
        
        # Translation/Language commands
        elif "translate" in command_text or "how do you say" in command_text or "learn" in command_text:
            response = multilang_commands.handle_command(command_text)
        
        # Automation commands
        elif "remind me" in command_text or "list tasks" in command_text or "cancel task" in command_text:
            response = automation_commands.handle_command(command_text)
        
        # Fun commands
        elif "joke" in command_text or "sing" in command_text or "funny" in command_text:
            response = fun_commands.handle_command(command_text)
        
        # Default to AI for general queries and conversations
        else:
            response = ai_commands.handle_command(command_text, self.nlp)
        
        return response
    
    def _extract_city(self, command):
        """Extract city name from weather command."""
        # Simple extraction - can be improved
        words = command.split()
        for i, word in enumerate(words):
            if word in ["in", "for", "at"]:
                if i + 1 < len(words):
                    return " ".join(words[i+1:])
        return "New York"  # Default city
    
    def _extract_symbol(self, command):
        """Extract stock symbol from command."""
        words = command.split()
        for word in words:
            if word.isupper() and len(word) <= 5:
                return word
        # Common stock names
        if "apple" in command:
            return "AAPL"
        elif "google" in command:
            return "GOOGL"
        elif "microsoft" in command:
            return "MSFT"
        elif "tesla" in command:
            return "TSLA"
        return "AAPL"  # Default
    
    def _extract_crypto_symbol(self, command):
        """Extract crypto symbol from command."""
        if "bitcoin" in command:
            return "BTC"
        elif "ethereum" in command:
            return "ETH"
        elif "dogecoin" in command:
            return "DOGE"
        return "BTC"  # Default
