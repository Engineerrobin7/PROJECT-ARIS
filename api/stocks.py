# api/stocks.py
"""
Stock market API integration for fetching stock prices and crypto data.
"""
import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join('config', 'config.env'))

class StocksAPI:
    def __init__(self):
        self.api_key = os.getenv("ALPHA_VANTAGE_API_KEY", "")
        self.base_url = "https://www.alphavantage.co/query"
    
    def get_stock_price(self, symbol):
        """
        Get current stock price for a symbol.
        
        Args:
            symbol (str): Stock symbol (e.g., 'AAPL', 'GOOGL')
        """
        if not self.api_key:
            return "Stock API key not configured. Please add ALPHA_VANTAGE_API_KEY to config.env"
        
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol.upper(),
            "apikey": self.api_key
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if "Global Quote" in data and data["Global Quote"]:
                quote = data["Global Quote"]
                price = quote.get("05. price", "N/A")
                change = quote.get("09. change", "N/A")
                change_percent = quote.get("10. change percent", "N/A")
                
                return (f"{symbol.upper()} is trading at ${price}. "
                       f"Change: {change} ({change_percent}).")
            else:
                return f"Could not find stock data for '{symbol}'."
        except Exception as e:
            return f"Error fetching stock data: {str(e)}"
    
    def get_crypto_price(self, symbol, currency="USD"):
        """Get cryptocurrency price."""
        if not self.api_key:
            return "Stock API key not configured."
        
        params = {
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": symbol.upper(),
            "to_currency": currency.upper(),
            "apikey": self.api_key
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if "Realtime Currency Exchange Rate" in data:
                rate_data = data["Realtime Currency Exchange Rate"]
                rate = rate_data.get("5. Exchange Rate", "N/A")
                
                return f"{symbol.upper()} is trading at ${rate} {currency}."
            else:
                return f"Could not find crypto data for '{symbol}'."
        except Exception as e:
            return f"Error fetching crypto data: {str(e)}"
