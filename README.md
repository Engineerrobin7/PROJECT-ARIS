# ARIS (Powered by Orion Engine)

**Tagline:** "Your AI companion that listens, learns, and speaks like a human."

## Overview
ARIS is an advanced desktop-based voice assistant inspired by J.A.R.V.I.S from Iron Man. It uses the Orion Engine, a modular AI core that combines speech recognition, natural language processing, and system control. ARIS can listen to your voice, execute commands, hold conversations, and even wake up with a personalized voice trigger ("Wake up ARIS").

## Core Goals
* Create a modular, extensible AI assistant framework.
* Integrate natural voice input/output.
* Enable real-world control (apps, web, files).
* Add GPT-powered reasoning and dialogue.
* Support emotion, tone, and custom personality.

## Key Features
| Feature | Description |
|---|---|
| Wake Word Detection | "Wake up ARIS" triggers active listening mode. |
| Voice Input (STT) | Converts your speech to text using `speech_recognition`. |
| Voice Output (TTS) | Speaks back naturally using `pyttsx3`. |
| Command Routing (Orion Engine) | Interprets user commands and routes them to proper modules. |
| System Control | Opens apps, websites, or executes shell commands. |
| AI Chat / Q&A | Uses GPT API for advanced reasoning and human-like conversation. |
| Fun Personality | Includes jokes, greetings, emotional tone. |
| Logging System | Tracks errors, commands, and responses. |
| Extensible Design | Easy to plug in new features like memory or GUI later. |

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

1. Start ARIS using the command above
2. Say "Wake up ARIS" to activate the assistant
3. When ARIS responds with "I'm listening", speak your command
4. Try commands like:
   - "What time is it?"
   - "Open Notepad"
   - "Search the web for Python tutorials"
   - "Tell me a joke"
   - "What is the capital of France?"

## Project Structure

```
├── assets/            # Sound files, voices, etc.
├── commands/          # Command modules (system, web, AI, fun)
├── config/            # Configuration files
├── core/              # Core modules (wake word, speech I/O)
├── logs/              # Log files
├── orion_engine/      # Brain, NLP, memory, personality
├── main.py            # Entry point
└── requirements.txt   # Dependencies
```

## Next Upgrade Phases
1.  **Core System:** Base setup (Wake word, STT, TTS)
2.  **Brain Power:** Orion Engine (Command routing, GPT)
3.  **Muscle Memory:** Commands (System, web, fun)
4.  **Intelligence Boost:** AI Memory (Contextual awareness)
5.  **Personality Layer:** Voice + Tone (Dynamic emotions)
6.  **Visual Interface:** GUI (Desktop dashboard for ARIS)
7.  **Integration Layer:** IoT + Mobile (Control external devices)

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
