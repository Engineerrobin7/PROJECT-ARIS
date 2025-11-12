# ARIS Usage Guide

Complete guide to using all features of ARIS Assistant.

## 🚀 Getting Started

### Starting ARIS

**Option 1: GUI Mode (Recommended)**
```bash
python gui_enhanced.py
```

**Option 2: Voice Mode**
```bash
python main.py
```

**Option 3: Background Service**
```bash
start_aris.bat
```

---

## 🎤 Voice Commands

### System Commands

**Opening Applications:**
- "Open Notepad"
- "Start Calculator"
- "Run File Explorer"
- "Open Browser"

**Closing Applications:**
- "Close Notepad"
- "Exit Calculator"

**System Information:**
- "What time is it?"
- "What's the date?"
- "Tell me the time and date"

---

### 🌐 Web & Search Commands

**Web Search:**
- "Search Google for Python tutorials"
- "Find information about AI"
- "Google machine learning"

**Wikipedia:**
- "Wikipedia search for Albert Einstein"
- "Tell me about the Eiffel Tower"
- "What is quantum physics?"

**YouTube:**
- "Play Bohemian Rhapsody on YouTube"
- "Search YouTube for cooking videos"
- "Play music by The Beatles"

---

### 🌤️ Weather Commands

**Current Weather:**
- "What's the weather in New York?"
- "Tell me the weather in London"
- "How's the weather in Tokyo?"

**Forecast:**
- "Give me the forecast for Paris"
- "Weather forecast for Los Angeles"

---

### 📰 News Commands

**Headlines:**
- "What's the latest news?"
- "Tell me today's headlines"
- "What's happening in the world?"

**Topic Search:**
- "News about technology"
- "Tell me news about sports"
- "What's the news on climate change?"

---

### 💰 Financial Commands

**Stock Prices:**
- "What's the price of Apple stock?"
- "Check Tesla stock"
- "How's Microsoft doing?"
- "Stock price for GOOGL"

**Cryptocurrency:**
- "What's the Bitcoin price?"
- "Check Ethereum"
- "How much is Dogecoin?"

---

### 🏀 Sports Commands

**Scores:**
- "Show me NBA scores"
- "What are today's games?"
- "Give me sports scores"

---

### 📅 Calendar Commands

**Add Events:**
- "Add event meeting on 2025-11-15"
- "Schedule dentist appointment on 2025-11-20 at 14:00"

**View Events:**
- "Show my calendar"
- "What events do I have?"
- "Show upcoming events"

**Delete Events:**
- "Delete event 1"
- "Cancel event 3"

---

### 📧 Email Commands

**Check Email:**
- "Check my email"
- "Do I have unread messages?"
- "Show my emails"

**Note:** Sending emails requires additional setup through GUI

---

### 🎮 Game Commands

**Number Guessing:**
- "Let's play a number game"
- "Start number game"
- Then guess: "Is it 50?"

**Coin Flip:**
- "Flip a coin"
- "Heads or tails?"

**Dice Roll:**
- "Roll the dice"
- "Roll a dice"

**Magic 8 Ball:**
- "Magic 8 ball, will I succeed?"
- "Ask the 8 ball"

**Trivia:**
- "Ask me a trivia question"
- "Give me a quiz"

---

### 🌍 Translation Commands

**Translate Phrases:**
- "Translate hello to Spanish"
- "How do you say thank you in French?"
- "Translate goodbye to German"

**Language Lessons:**
- "Teach me basic Spanish"
- "Learn French phrases"
- "Show me German basics"

**Supported Languages:**
- Spanish, French, German, Italian
- Portuguese, Russian, Japanese
- Chinese, Korean, Arabic

---

### 🤖 Automation Commands

**Set Reminders:**
- "Remind me to call John tomorrow"
- "Schedule a reminder for 3 PM"

**Task Management:**
- "List my tasks"
- "Show my reminders"
- "Cancel task 2"

---

### 🎭 Fun Commands

**Jokes:**
- "Tell me a joke"
- "Make me laugh"
- "Say something funny"

**Songs:**
- "Sing a song"
- "Sing me something"

**Greetings:**
- "Hello ARIS"
- "Hi there"
- "Good morning"

**Thanks:**
- "Thank you"
- "Thanks ARIS"

---

### 💬 AI Conversation

**General Questions:**
- "What is artificial intelligence?"
- "Explain quantum computing"
- "Tell me about space exploration"

**Creative Tasks:**
- "Write a poem about nature"
- "Create a story about robots"
- "Generate ideas for a birthday party"

**Advice:**
- "Give me productivity tips"
- "How can I learn programming?"
- "What should I do today?"

---

## 🖥️ GUI Usage

### Chat Interface

1. **Text Input:**
   - Type your command in the input field
   - Press Enter or click "Send"

2. **Voice Input:**
   - Click the "🎤 Voice" button
   - Speak your command
   - Click "⏹ Stop" when done

3. **View History:**
   - Scroll through the chat window
   - See timestamps for each message
   - Color-coded messages (You: Green, ARIS: Blue)

### Status Bar
- Shows current status (Ready, Listening, Processing)
- Displays errors if they occur

---

## ⚙️ Configuration

### User Settings

Edit `config/config.env`:

```env
# Change your name
USER_NAME=YourName

# Customize wake word
WAKE_WORD="hey assistant"

# Adjust voice speed
VOICE_RATE=170

# Adjust voice volume (0.0 to 1.0)
VOICE_VOLUME=1.0
```

### API Configuration

See [API_SETUP_GUIDE.md](API_SETUP_GUIDE.md) for detailed API setup instructions.

---

## 🔍 Tips & Tricks

### Best Practices

1. **Speak Clearly:** Enunciate words for better recognition
2. **Use Keywords:** Include action words (open, search, play, etc.)
3. **Be Specific:** "Weather in Paris" vs "Weather"
4. **Check Logs:** View `logs/aris.log` for troubleshooting

### Command Patterns

Most commands follow these patterns:
- **Action + Object:** "Open Notepad"
- **Question:** "What's the weather?"
- **Request:** "Tell me a joke"
- **Search:** "Search for Python"

### Shortcuts

- Press Enter to send text commands
- Use arrow keys to navigate chat history
- Ctrl+C to stop voice mode

---

## 🐛 Troubleshooting

### Voice Not Working
1. Check microphone permissions
2. Verify PyAudio installation
3. Test with text commands first
4. Check system audio settings

### API Errors
1. Verify API keys in config.env
2. Check internet connection
3. Ensure API service is active
4. Review rate limits

### Application Not Opening
1. Check application name spelling
2. Verify application is installed
3. Try full application path
4. Check system permissions

---

## 📊 Command Examples by Category

### Quick Reference

**System:**
- "Open Calculator"
- "What time is it?"

**Web:**
- "Search Google for recipes"
- "Play music on YouTube"

**Information:**
- "Weather in London"
- "Latest news"
- "Apple stock price"

**Entertainment:**
- "Tell me a joke"
- "Flip a coin"
- "Play a game"

**Productivity:**
- "Add calendar event"
- "Check my email"
- "Remind me later"

**Learning:**
- "Translate hello to Spanish"
- "Teach me French"

---

## 🎯 Advanced Usage

### Chaining Commands

While ARIS processes one command at a time, you can:
1. Use the GUI to queue multiple commands
2. Create automation tasks for recurring actions
3. Use calendar events for scheduled commands

### Personalization

ARIS learns from your interactions:
- Frequently used commands are recognized faster
- Preferences are saved automatically
- Conversation history helps with context

### Custom Workflows

Create custom automation tasks:
1. "Schedule reminder to check email at 9 AM"
2. "Add task to review news daily"

---

## 📱 Mobile & Remote Access

**Coming Soon:**
- Mobile app integration
- Remote voice commands
- Cloud synchronization

---

## 🆘 Getting Help

1. **Check Documentation:**
   - README.md
   - FEATURES.md
   - API_SETUP_GUIDE.md

2. **View Logs:**
   - `logs/aris.log`

3. **Test Components:**
   - Run `test_aris.py`

4. **Community:**
   - GitHub Issues
   - Discussion Forums

---

## 🎓 Learning Resources

### Tutorials
- Voice command basics
- API integration guide
- Custom command creation
- GUI customization

### Examples
- See `tests/` directory for code examples
- Check `commands/` for command implementations
- Review `api/` for API integration patterns

---

**Happy Assisting! 🚀**

For more information, visit the [GitHub repository](https://github.com/yourusername/aris).
