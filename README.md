# ARIS (Powered by Orion Engine)

**Tagline:** "Your AI companion that listens, learns, and speaks like a human."

## Overview
ARIS is an advanced desktop-based voice assistant inspired by J.A.R.V.I.S from Iron Man. It uses the Orion Engine, a modular AI core that combines speech recognition, natural language processing, and system control. ARIS can listen to your voice, execute commands, hold conversations, and even wake up with a personalized voice trigger ("Wake up ARIS").

## 🌟 What's New

ARIS now includes **comprehensive enhancements** with 50+ new features:

### 🚀 New API Integrations
- **Weather API** - Real-time weather and forecasts
- **News API** - Latest headlines and topic search
- **Wikipedia API** - Quick facts and summaries
- **YouTube API** - Video search and playback
- **Stock Market API** - Real-time stock and crypto prices
- **Sports API** - Live scores and schedules
- **Calendar API** - Event management and reminders
- **Email API** - Check and send emails

### 🎮 Entertainment & Games
- Number guessing game
- Coin flip & dice rolling
- Magic 8 Ball
- Trivia questions
- Enhanced jokes and fun commands

### 🌍 Multi-Language Support
- Translation for 10+ languages
- Language learning features
- Common phrase dictionary
- Support for Spanish, French, German, Italian, Portuguese, Russian, Japanese, Chinese, Korean, Arabic

### 🤖 Automation & Productivity
- Task scheduling and reminders
- Automation workflows
- Smart task management
- Recurring tasks

### 🎨 Enhanced GUI
- Modern dark theme interface
- Chat-style conversation view
- Voice input button
- Real-time status indicators
- Scrollable history

### 🧠 Advanced Intelligence
- Persistent memory with SQLite database
- User preference learning
- Conversation history
- Personalization engine
- Context awareness

## Core Goals
* Create a modular, extensible AI assistant framework.
* Integrate natural voice input/output.
* Enable real-world control (apps, web, files).
* Add GPT-powered reasoning and dialogue.
* Support emotion, tone, and custom personality.
* Provide comprehensive API integrations.
* Enable multi-language support and translation.
* Offer entertainment and productivity features.

## Key Features
| Feature | Description |
|---|---|
| Wake Word Detection | "Wake up ARIS" triggers active listening mode. |
| Voice Input (STT) | Converts your speech to text using `speech_recognition`. |
| Voice Output (TTS) | Speaks back naturally using `pyttsx3`. |
| Command Routing (Orion Engine) | Interprets user commands and routes them to proper modules. |
| System Control | Opens apps, websites, or executes shell commands. |
| AI Chat / Q&A | Uses GPT API for advanced reasoning and human-like conversation. |
| Weather & News | Real-time weather, forecasts, and latest news headlines. |
| Entertainment | Games, jokes, music, and fun interactions. |
| Multi-Language | Translation and language learning for 10+ languages. |
| Automation | Task scheduling, reminders, and workflow automation. |
| Email Integration | Check unread emails and send messages. |
| Stock Market | Real-time stock prices and cryptocurrency tracking. |
| Calendar | Event management and scheduling. |
| Database Memory | Persistent storage with SQLite for learning and personalization. |
| Enhanced GUI | Modern interface with chat view and voice controls. |
| Logging System | Tracks errors, commands, and responses. |
| Extensible Design | Easy to plug in new features and APIs. |

## Tech Stack
* **Language:** Python 3.11+
* **Libraries:** `speechrecognition`, `pyttsx3`, `pyaudio`, `openai`, `python-dotenv`, `requests`
* **Platform:** Windows/Linux/macOS

## Installation

### Prerequisites
- Python 3.11 or higher
- An OpenAI API key for GPT integration

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/aris.git
   cd aris
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your environment:
   - Copy `config/config.env` and update with your OpenAI API key
   - Adjust settings in `config/settings.py` if needed

5. Run ARIS:
   ```bash
   python main.py
   ```

## Usage

### Starting ARIS

**GUI Mode (Recommended):**
```bash
python gui_enhanced.py
```

**Voice Mode:**
```bash
python main.py
```

### Example Commands

**System Control:**
- "Open Notepad"
- "What time is it?"
- "Close Calculator"

**Web & Information:**
- "Search Google for Python tutorials"
- "Wikipedia search for Albert Einstein"
- "Play Bohemian Rhapsody on YouTube"

**Weather & News:**
- "What's the weather in New York?"
- "Give me the forecast for London"
- "What's the latest news?"
- "Tell me news about technology"

**Financial:**
- "What's the price of Apple stock?"
- "Check Bitcoin price"
- "How's Tesla doing?"

**Entertainment:**
- "Tell me a joke"
- "Let's play a number game"
- "Flip a coin"
- "Magic 8 ball, will I succeed?"

**Translation:**
- "Translate hello to Spanish"
- "How do you say thank you in French?"
- "Teach me basic German"

**Productivity:**
- "Check my email"
- "Show my calendar"
- "Remind me to call John tomorrow"

**AI Conversation:**
- "What is artificial intelligence?"
- "Write a poem about nature"
- "Give me productivity tips"

For complete command list, see [USAGE_GUIDE.md](USAGE_GUIDE.md)

## Project Structure

```
├── api/                      # API integrations
│   ├── calendar_api.py      # Calendar management
│   ├── email_api.py         # Email integration
│   ├── news.py              # News API
│   ├── sports.py            # Sports scores
│   ├── stocks.py            # Stock market data
│   ├── weather.py           # Weather information
│   ├── wikipedia.py         # Wikipedia search
│   └── youtube.py           # YouTube integration
├── commands/                 # Command modules
│   ├── ai_commands.py       # AI-powered commands
│   ├── automation_commands.py # Task automation
│   ├── fun_commands.py      # Entertainment commands
│   ├── games_commands.py    # Interactive games
│   ├── multilang_commands.py # Translation & languages
│   ├── system_commands.py   # System control
│   └── web_commands.py      # Web operations
├── config/                   # Configuration files
│   ├── config.env           # Environment variables
│   └── settings.py          # Settings module
├── core/                     # Core modules
│   ├── manager.py           # Core manager
│   ├── nlu.py               # Natural language understanding
│   ├── speech_input.py      # Speech recognition
│   ├── speech_output.py     # Text-to-speech
│   └── wake_word.py         # Wake word detection
├── data/                     # Data storage
│   ├── aris.db              # SQLite database
│   ├── calendar.json        # Calendar events
│   └── automation_tasks.json # Scheduled tasks
├── logs/                     # Log files
│   └── aris.log             # Application logs
├── orion_engine/            # AI engine
│   ├── brain.py             # Command routing
│   ├── database.py          # Database management
│   ├── memory.py            # Memory system
│   ├── nlp_module.py        # NLP processing
│   └── personality.py       # Personality traits
├── gui_enhanced.py          # Enhanced GUI
├── main.py                  # Voice mode entry point
├── requirements.txt         # Dependencies
├── API_SETUP_GUIDE.md       # API configuration guide
├── FEATURES.md              # Complete feature list
└── USAGE_GUIDE.md           # Detailed usage instructions
```

## Documentation

- **[FEATURES.md](FEATURES.md)** - Complete list of all features
- **[API_SETUP_GUIDE.md](API_SETUP_GUIDE.md)** - Step-by-step API configuration
- **[USAGE_GUIDE.md](USAGE_GUIDE.md)** - Detailed usage instructions and examples
- **[HOW_TO_START_ARIS.md](HOW_TO_START_ARIS.md)** - Quick start guide

## Upgrade Status

✅ **Completed Phases:**
1.  **Core System:** Wake word, STT, TTS ✓
2.  **Brain Power:** Orion Engine with command routing ✓
3.  **Muscle Memory:** System, web, AI, and fun commands ✓
4.  **Intelligence Boost:** Database memory and personalization ✓
5.  **Personality Layer:** Dynamic responses and emotions ✓
6.  **Visual Interface:** Enhanced GUI with modern design ✓
7.  **API Integration:** Weather, news, stocks, sports, email, calendar ✓
8.  **Entertainment:** Games, jokes, music ✓
9.  **Multi-Language:** Translation and language learning ✓
10. **Automation:** Task scheduling and reminders ✓

🚀 **Future Enhancements:**
- IoT device control
- Mobile app integration
- Cloud synchronization
- Voice customization
- Plugin system
- Video call integration
- Gesture recognition

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
