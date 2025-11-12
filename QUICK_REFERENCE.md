# ARIS Quick Reference

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Configure API keys
# Edit config/config.env with your API keys

# Launch GUI (Recommended)
python gui_enhanced.py

# Or launch voice mode
python main.py

# Or use quick start wizard
python quick_start.py
```

## 📋 Essential Commands

### System
- "Open [app]" - Open application
- "What time is it?" - Get time/date
- "Close [app]" - Close application

### Information
- "Weather in [city]" - Get weather
- "Latest news" - Get headlines
- "Wikipedia [topic]" - Search Wikipedia
- "[SYMBOL] stock price" - Get stock price

### Entertainment
- "Tell me a joke" - Get a joke
- "Play [song] on YouTube" - Play video
- "Flip a coin" - Coin flip
- "Number game" - Play game

### Productivity
- "Check my email" - Check emails
- "Show calendar" - View events
- "Remind me [task]" - Set reminder

### Translation
- "Translate [text] to [language]"
- "How do you say [phrase] in [language]"

## 📚 Documentation

- **FEATURES.md** - All features
- **API_SETUP_GUIDE.md** - API setup
- **USAGE_GUIDE.md** - Detailed usage
- **CHANGELOG.md** - What's new

## 🔑 API Keys Needed

1. OpenAI - AI conversations
2. OpenWeatherMap - Weather
3. NewsAPI - News headlines
4. Alpha Vantage - Stocks
5. YouTube - Video search (optional)
6. Sports API - Scores (optional)

## 🆘 Troubleshooting

**Voice not working?**
- Check microphone permissions
- Verify PyAudio installed

**API errors?**
- Check API keys in config.env
- Verify internet connection

**App won't start?**
- Run: `python quick_start.py`
- Check logs in `logs/aris.log`

## 💡 Tips

- Start with GUI mode for easier use
- Configure one API at a time
- Check logs for detailed errors
- Use text commands to test features
