# API Setup Guide for ARIS

This guide will help you set up all the API integrations for ARIS.

## 📋 Table of Contents
1. [OpenAI API](#openai-api)
2. [Weather API](#weather-api)
3. [News API](#news-api)
4. [YouTube API](#youtube-api)
5. [Stock Market API](#stock-market-api)
6. [Sports API](#sports-api)
7. [Email Configuration](#email-configuration)

---

## 🤖 OpenAI API

**Purpose:** Powers AI conversations and natural language understanding

### Setup Steps:
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy the key and add to `config/config.env`:
   ```
   OPENAI_API_KEY=sk-your-key-here
   ```

**Cost:** Pay-as-you-go (starts free with credits)

---

## 🌤️ Weather API

**Purpose:** Get weather information and forecasts

### Setup Steps:
1. Go to [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to API Keys
4. Copy your API key
5. Add to `config/config.env`:
   ```
   WEATHER_API_KEY=your-key-here
   ```

**Cost:** Free tier available (60 calls/minute)

**Commands:**
- "What's the weather in [city]?"
- "Give me the forecast for [city]"

---

## 📰 News API

**Purpose:** Fetch latest news headlines and articles

### Setup Steps:
1. Go to [NewsAPI](https://newsapi.org/)
2. Sign up for a free account
3. Get your API key from the dashboard
4. Add to `config/config.env`:
   ```
   NEWS_API_KEY=your-key-here
   ```

**Cost:** Free tier (100 requests/day)

**Commands:**
- "What's the latest news?"
- "Tell me news about [topic]"

---

## 🎥 YouTube API

**Purpose:** Search and play YouTube videos

### Setup Steps:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable YouTube Data API v3
4. Create credentials (API Key)
5. Add to `config/config.env`:
   ```
   YOUTUBE_API_KEY=your-key-here
   ```

**Note:** ARIS can work without this key using direct search URLs

**Cost:** Free tier (10,000 units/day)

**Commands:**
- "Play [song/video] on YouTube"
- "Search YouTube for [query]"

---

## 📈 Stock Market API

**Purpose:** Get real-time stock and cryptocurrency prices

### Setup Steps:
1. Go to [Alpha Vantage](https://www.alphavantage.co/)
2. Get your free API key
3. Add to `config/config.env`:
   ```
   ALPHA_VANTAGE_API_KEY=your-key-here
   ```

**Cost:** Free tier (5 API calls/minute, 500/day)

**Commands:**
- "What's the price of [SYMBOL] stock?"
- "Check Bitcoin price"

---

## 🏀 Sports API

**Purpose:** Get sports scores and schedules

### Setup Steps:
1. Go to [The Odds API](https://the-odds-api.com/)
2. Sign up for a free account
3. Get your API key
4. Add to `config/config.env`:
   ```
   SPORTS_API_KEY=your-key-here
   ```

**Cost:** Free tier (500 requests/month)

**Commands:**
- "Show me NBA scores"
- "What are today's games?"

---

## 📧 Email Configuration

**Purpose:** Check and send emails

### Gmail Setup:
1. Enable 2-Factor Authentication on your Google account
2. Generate an App Password:
   - Go to Google Account Settings
   - Security → 2-Step Verification → App passwords
   - Generate password for "Mail"
3. Add to `config/config.env`:
   ```
   EMAIL_ADDRESS=your-email@gmail.com
   EMAIL_PASSWORD=your-app-password-here
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   IMAP_SERVER=imap.gmail.com
   ```

### Other Email Providers:
- **Outlook/Hotmail:**
  ```
  SMTP_SERVER=smtp-mail.outlook.com
  SMTP_PORT=587
  IMAP_SERVER=outlook.office365.com
  ```

- **Yahoo:**
  ```
  SMTP_SERVER=smtp.mail.yahoo.com
  SMTP_PORT=587
  IMAP_SERVER=imap.mail.yahoo.com
  ```

**Commands:**
- "Check my email"
- "Do I have unread messages?"

---

## 🔧 Configuration File

Your complete `config/config.env` should look like this:

```env
# OpenAI API key for GPT integration
OPENAI_API_KEY=sk-your-key-here

# User information
USER_NAME=YourName

# Voice assistant settings
WAKE_WORD="wake up aris"
VOICE_RATE=170
VOICE_VOLUME=1.0

# Logging settings
LOG_LEVEL=INFO

# NLP settings
MAX_TOKENS=150
TEMPERATURE=0.7

# API Keys for integrations
WEATHER_API_KEY=your-openweathermap-key
NEWS_API_KEY=your-newsapi-key
YOUTUBE_API_KEY=your-youtube-key
ALPHA_VANTAGE_API_KEY=your-alphavantage-key
SPORTS_API_KEY=your-sports-api-key

# Email configuration
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
IMAP_SERVER=imap.gmail.com
```

---

## ✅ Testing Your Setup

After configuring all APIs, test them with these commands:

1. **Weather:** "What's the weather in New York?"
2. **News:** "What's the latest news?"
3. **Wikipedia:** "Tell me about Python programming"
4. **YouTube:** "Play Bohemian Rhapsody"
5. **Stocks:** "What's Apple stock price?"
6. **Email:** "Check my email"

---

## 🆘 Troubleshooting

### API Key Not Working
- Verify the key is copied correctly (no extra spaces)
- Check if the API service is active
- Ensure you haven't exceeded rate limits

### Email Not Working
- Verify 2FA is enabled
- Use App Password, not regular password
- Check firewall/antivirus settings

### Voice Commands Not Recognized
- Check microphone permissions
- Ensure PyAudio is installed correctly
- Test with text commands first

---

## 💡 Tips

1. **Start with free tiers** - Most APIs offer generous free tiers
2. **Monitor usage** - Keep track of API call limits
3. **Secure your keys** - Never commit API keys to public repositories
4. **Test incrementally** - Set up one API at a time
5. **Use fallbacks** - ARIS works even without some APIs configured

---

## 📚 Additional Resources

- [OpenAI Documentation](https://platform.openai.com/docs)
- [OpenWeatherMap API Docs](https://openweathermap.org/api)
- [NewsAPI Documentation](https://newsapi.org/docs)
- [YouTube API Guide](https://developers.google.com/youtube/v3)
- [Alpha Vantage Docs](https://www.alphavantage.co/documentation/)

---

**Need Help?** Check the logs in `logs/aris.log` for detailed error messages.
