#!/usr/bin/env python3
# test_all_features.py
"""
Comprehensive test suite for all ARIS features.
"""
import sys
import os

def test_api_integrations():
    """Test all API integrations."""
    print("\n" + "=" * 60)
    print("Testing API Integrations")
    print("=" * 60)
    
    # Test Weather API
    print("\n1. Testing Weather API...")
    try:
        from api.weather import WeatherAPI
        weather = WeatherAPI()
        result = weather.get_weather("London")
        print(f"   Result: {result[:100]}...")
        print("   ✓ Weather API working")
    except Exception as e:
        print(f"   ✗ Weather API error: {str(e)}")
    
    # Test News API
    print("\n2. Testing News API...")
    try:
        from api.news import NewsAPI
        news = NewsAPI()
        result = news.get_top_headlines()
        print(f"   Result: {result[:100]}...")
        print("   ✓ News API working")
    except Exception as e:
        print(f"   ✗ News API error: {str(e)}")
    
    # Test Wikipedia API
    print("\n3. Testing Wikipedia API...")
    try:
        from api.wikipedia import WikipediaAPI
        wiki = WikipediaAPI()
        result = wiki.search("Python programming")
        print(f"   Result: {result[:100]}...")
        print("   ✓ Wikipedia API working")
    except Exception as e:
        print(f"   ✗ Wikipedia API error: {str(e)}")
    
    # Test YouTube API
    print("\n4. Testing YouTube API...")
    try:
        from api.youtube import YouTubeAPI
        youtube = YouTubeAPI()
        print("   ✓ YouTube API initialized")
    except Exception as e:
        print(f"   ✗ YouTube API error: {str(e)}")
    
    # Test Stocks API
    print("\n5. Testing Stocks API...")
    try:
        from api.stocks import StocksAPI
        stocks = StocksAPI()
        result = stocks.get_stock_price("AAPL")
        print(f"   Result: {result[:100]}...")
        print("   ✓ Stocks API working")
    except Exception as e:
        print(f"   ✗ Stocks API error: {str(e)}")
    
    # Test Calendar API
    print("\n6. Testing Calendar API...")
    try:
        from api.calendar_api import CalendarAPI
        calendar = CalendarAPI()
        result = calendar.get_events()
        print(f"   Result: {result}")
        print("   ✓ Calendar API working")
    except Exception as e:
        print(f"   ✗ Calendar API error: {str(e)}")

def test_command_modules():
    """Test all command modules."""
    print("\n" + "=" * 60)
    print("Testing Command Modules")
    print("=" * 60)
    
    # Test System Commands
    print("\n1. Testing System Commands...")
    try:
        from commands import system_commands
        result = system_commands.get_time_date()
        print(f"   Result: {result}")
        print("   ✓ System commands working")
    except Exception as e:
        print(f"   ✗ System commands error: {str(e)}")
    
    # Test Fun Commands
    print("\n2. Testing Fun Commands...")
    try:
        from commands import fun_commands
        result = fun_commands.handle_command("tell me a joke")
        print(f"   Result: {result[:100]}...")
        print("   ✓ Fun commands working")
    except Exception as e:
        print(f"   ✗ Fun commands error: {str(e)}")
    
    # Test Games Commands
    print("\n3. Testing Games Commands...")
    try:
        from commands import games_commands
        result = games_commands.handle_command("flip a coin")
        print(f"   Result: {result}")
        print("   ✓ Games commands working")
    except Exception as e:
        print(f"   ✗ Games commands error: {str(e)}")
    
    # Test Multi-Language Commands
    print("\n4. Testing Multi-Language Commands...")
    try:
        from commands import multilang_commands
        result = multilang_commands.handle_command("translate hello to spanish")
        print(f"   Result: {result}")
        print("   ✓ Multi-language commands working")
    except Exception as e:
        print(f"   ✗ Multi-language commands error: {str(e)}")
    
    # Test Automation Commands
    print("\n5. Testing Automation Commands...")
    try:
        from commands import automation_commands
        result = automation_commands.handle_command("list tasks")
        print(f"   Result: {result}")
        print("   ✓ Automation commands working")
    except Exception as e:
        print(f"   ✗ Automation commands error: {str(e)}")

def test_orion_engine():
    """Test Orion Engine components."""
    print("\n" + "=" * 60)
    print("Testing Orion Engine")
    print("=" * 60)
    
    # Test Brain
    print("\n1. Testing Brain...")
    try:
        from orion_engine.brain import Brain
        brain = Brain()
        result = brain.route_command("what time is it")
        print(f"   Result: {result}")
        print("   ✓ Brain working")
    except Exception as e:
        print(f"   ✗ Brain error: {str(e)}")
    
    # Test Memory
    print("\n2. Testing Memory...")
    try:
        from orion_engine.memory import Memory
        memory = Memory()
        memory.add_to_history("test command")
        print("   ✓ Memory working")
    except Exception as e:
        print(f"   ✗ Memory error: {str(e)}")
    
    # Test Database
    print("\n3. Testing Database...")
    try:
        from orion_engine.database import Database
        db = Database()
        db.save_preference("test_key", "test_value")
        value = db.get_preference("test_key")
        print(f"   Saved and retrieved: {value}")
        print("   ✓ Database working")
        db.close()
    except Exception as e:
        print(f"   ✗ Database error: {str(e)}")
    
    # Test Personality
    print("\n4. Testing Personality...")
    try:
        from orion_engine.personality import Personality
        personality = Personality()
        joke = personality.get_joke()
        print(f"   Joke: {joke[:100]}...")
        print("   ✓ Personality working")
    except Exception as e:
        print(f"   ✗ Personality error: {str(e)}")

def test_core_modules():
    """Test core modules."""
    print("\n" + "=" * 60)
    print("Testing Core Modules")
    print("=" * 60)
    
    # Test TTS
    print("\n1. Testing Text-to-Speech...")
    try:
        from core.speech_output import TTSEngine
        tts = TTSEngine()
        print("   ✓ TTS engine initialized")
    except Exception as e:
        print(f"   ✗ TTS error: {str(e)}")
    
    # Test Speech Input
    print("\n2. Testing Speech Input...")
    try:
        from core.speech_input import SpeechInput
        speech = SpeechInput()
        print("   ✓ Speech input initialized")
    except Exception as e:
        print(f"   ✗ Speech input error: {str(e)}")

def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("  ARIS - Comprehensive Feature Test Suite")
    print("=" * 60)
    
    try:
        test_core_modules()
        test_orion_engine()
        test_command_modules()
        test_api_integrations()
        
        print("\n" + "=" * 60)
        print("  Test Suite Complete!")
        print("=" * 60)
        print("\n✅ All tests completed. Check results above for any errors.")
        print("\nNote: Some API tests may fail if API keys are not configured.")
        print("See API_SETUP_GUIDE.md for configuration instructions.\n")
        
    except KeyboardInterrupt:
        print("\n\nTests interrupted by user.")
    except Exception as e:
        print(f"\n\n❌ Test suite error: {str(e)}")

if __name__ == "__main__":
    main()
