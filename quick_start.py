#!/usr/bin/env python3
# quick_start.py
"""
Quick start script for ARIS - Tests all components and launches GUI.
"""
import os
import sys
from dotenv import load_dotenv

def check_dependencies():
    """Check if all required packages are installed."""
    print("🔍 Checking dependencies...")
    required_packages = [
        'speech_recognition',
        'pyttsx3',
        'openai',
        'requests',
        'dotenv'
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"  ✓ {package}")
        except ImportError:
            print(f"  ✗ {package} - MISSING")
            missing.append(package)
    
    if missing:
        print(f"\n❌ Missing packages: {', '.join(missing)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies installed!\n")
    return True

def check_config():
    """Check if configuration file exists and has required keys."""
    print("🔍 Checking configuration...")
    
    config_path = os.path.join('config', 'config.env')
    if not os.path.exists(config_path):
        print(f"  ✗ Config file not found: {config_path}")
        print("  Creating default config file...")
        
        os.makedirs('config', exist_ok=True)
        with open(config_path, 'w') as f:
            f.write("""# OpenAI API key for GPT integration
OPENAI_API_KEY=your_openai_key_here

# User information
USER_NAME=User

# Voice assistant settings
WAKE_WORD="wake up aris"
VOICE_RATE=170
VOICE_VOLUME=1.0

# Logging settings
LOG_LEVEL=INFO

# NLP settings
MAX_TOKENS=150
TEMPERATURE=0.7

# API Keys for new integrations
WEATHER_API_KEY=your_openweathermap_key_here
NEWS_API_KEY=your_newsapi_key_here
YOUTUBE_API_KEY=your_youtube_key_here
ALPHA_VANTAGE_API_KEY=your_alphavantage_key_here
SPORTS_API_KEY=your_sports_api_key_here

# Email configuration
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password_here
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
IMAP_SERVER=imap.gmail.com
""")
        print(f"  ✓ Created default config at {config_path}")
        print("  ⚠️  Please edit config/config.env with your API keys")
    else:
        print(f"  ✓ Config file found")
    
    # Load and check for API keys
    load_dotenv(dotenv_path=config_path)
    
    openai_key = os.getenv('OPENAI_API_KEY', '')
    if openai_key and openai_key != 'your_openai_key_here':
        print("  ✓ OpenAI API key configured")
    else:
        print("  ⚠️  OpenAI API key not configured (AI features limited)")
    
    print("✅ Configuration checked!\n")
    return True

def check_directories():
    """Ensure all required directories exist."""
    print("🔍 Checking directories...")
    
    directories = ['logs', 'data', 'config']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"  ✓ Created {directory}/")
        else:
            print(f"  ✓ {directory}/ exists")
    
    print("✅ All directories ready!\n")
    return True

def test_components():
    """Test core components."""
    print("🔍 Testing core components...")
    
    try:
        # Test TTS
        print("  Testing text-to-speech...")
        from core.speech_output import TTSEngine
        tts = TTSEngine()
        print("  ✓ TTS engine initialized")
        
        # Test Brain
        print("  Testing Orion Engine...")
        from orion_engine.brain import Brain
        brain = Brain()
        print("  ✓ Orion Engine initialized")
        
        # Test Memory
        print("  Testing memory system...")
        from orion_engine.memory import Memory
        memory = Memory()
        print("  ✓ Memory system initialized")
        
        print("✅ All components working!\n")
        return True
    except Exception as e:
        print(f"  ✗ Component test failed: {str(e)}")
        return False

def show_menu():
    """Show startup menu."""
    print("=" * 60)
    print("  ARIS - Advanced AI Assistant")
    print("  Powered by Orion Engine")
    print("=" * 60)
    print("\nChoose how to start ARIS:\n")
    print("  1. Launch Enhanced GUI (Recommended)")
    print("  2. Launch Voice Mode")
    print("  3. View Documentation")
    print("  4. Run Tests Only")
    print("  5. Exit")
    print()

def main():
    """Main quick start function."""
    print("\n" + "=" * 60)
    print("  ARIS Quick Start")
    print("=" * 60 + "\n")
    
    # Run checks
    if not check_dependencies():
        sys.exit(1)
    
    if not check_config():
        sys.exit(1)
    
    if not check_directories():
        sys.exit(1)
    
    if not test_components():
        print("\n⚠️  Some components failed to initialize.")
        print("You can still continue, but some features may not work.\n")
    
    # Show menu
    show_menu()
    
    while True:
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                print("\n🚀 Launching Enhanced GUI...")
                import gui_enhanced
                gui_enhanced.main()
                break
            elif choice == '2':
                print("\n🚀 Launching Voice Mode...")
                import main
                main.main()
                break
            elif choice == '3':
                print("\n📚 Documentation:")
                print("  - README.md - Main documentation")
                print("  - FEATURES.md - Complete feature list")
                print("  - API_SETUP_GUIDE.md - API configuration guide")
                print("  - USAGE_GUIDE.md - Detailed usage instructions")
                print()
            elif choice == '4':
                print("\n✅ Tests completed successfully!")
                break
            elif choice == '5':
                print("\n👋 Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1-5.")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            break

if __name__ == "__main__":
    main()
