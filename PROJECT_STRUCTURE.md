# ARIS Project Structure

## Complete Directory Layout

```
ARIS/
│
├── 📁 api/                          # API Integrations
│   ├── calendar_api.py             # Calendar management
│   ├── email_api.py                # Email integration
│   ├── news.py                     # News API
│   ├── sports.py                   # Sports scores
│   ├── stocks.py                   # Stock market data
│   ├── weather.py                  # Weather information
│   ├── wikipedia.py                # Wikipedia search
│   └── youtube.py                  # YouTube integration
│
├── 📁 commands/                     # Command Modules
│   ├── ai_commands.py              # AI-powered commands
│   ├── automation_commands.py      # Task automation
│   ├── fun_commands.py             # Entertainment commands
│   ├── games_commands.py           # Interactive games
│   ├── multilang_commands.py       # Translation & languages
│   ├── system_commands.py          # System control
│   └── web_commands.py             # Web operations
│
├── 📁 config/                       # Configuration
│   ├── config.env                  # Environment variables
│   ├── settings.py                 # Settings module
│   └── custom_commands.json        # User-defined commands
│
├── 📁 core/                         # Core Modules
│   ├── __init__.py
│   ├── manager.py                  # Core manager
│   ├── nlu.py                      # Natural language understanding
│   ├── speech_input.py             # Speech recognition
│   ├── speech_output.py            # Text-to-speech
│   └── wake_word.py                # Wake word detection
│
├── 📁 conversation/                 # Conversation Management
│   └── context_manager.py          # Context & history tracking
│
├── 📁 data/                         # Data Storage
│   ├── aris.db                     # SQLite database
│   ├── calendar.json               # Calendar events
│   ├── automation_tasks.json       # Scheduled tasks
│   ├── scheduled_tasks.json        # Advanced scheduler tasks
│   ├── conversation_history.json   # Conversation logs
│   └── file_operations_history.json # File operation logs
│
├── 📁 extensions/                   # Extensions
│   └── custom_commands.py          # Custom command manager
│
├── 📁 file_manager/                 # File Management System ⭐ NEW
│   ├── __init__.py
│   ├── file_operations.py          # Core file operations
│   ├── voice_commands.py           # Voice command handler
│   └── gui_file_manager.py         # GUI file manager
│
├── 📁 localization/                 # Multi-Language Support
│   ├── language_manager.py         # Language management
│   └── locales/                    # Translation files
│       ├── en.json                 # English
│       ├── es.json                 # Spanish
│       ├── fr.json                 # French
│       └── ...                     # Other languages
│
├── 📁 logs/                         # Log Files
│   ├── aris.log                    # Main application log
│   └── aris_enhanced.log           # Enhanced features log
│
├── 📁 orion_engine/                 # AI Engine
│   ├── brain.py                    # Command routing
│   ├── database.py                 # Database management
│   ├── memory.py                   # Memory system
│   ├── nlp_module.py               # NLP processing
│   └── personality.py              # Personality traits
│
├── 📁 plugins/                      # Plugin System ⭐ NEW
│   ├── __init__.py
│   ├── base_plugin.py              # Base plugin class
│   ├── plugin_manager.py           # Plugin manager
│   └── example_plugin.py           # Example plugin
│
├── 📁 scheduler/                    # Advanced Scheduler ⭐ NEW
│   └── advanced_scheduler.py       # Task scheduling system
│
├── 📁 skills/                       # Skills (Legacy)
│   └── ...                         # Various skill modules
│
├── 📁 smart_home/                   # Smart Home Integration ⭐ NEW
│   └── smart_home_controller.py    # Device control
│
├── 📁 src/                          # Source (Legacy)
│   └── ...                         # Legacy source files
│
├── 📁 tests/                        # Tests
│   ├── test_all_features.py
│   ├── test_aris.py
│   └── test_voice_simple.py
│
├── 📁 voice/                        # Voice Processing
│   └── ...                         # Voice-related modules
│
├── 📁 web_dashboard/                # Web Dashboard ⭐ NEW
│   ├── app.py                      # Flask application
│   ├── templates/
│   │   └── dashboard.html          # Dashboard UI
│   └── static/                     # Static assets (if any)
│
├── 📁 .vscode/                      # VS Code settings
├── 📁 __pycache__/                  # Python cache
├── 📁 venv/                         # Virtual environment
│
├── 📄 .env                          # Environment variables
├── 📄 .env.example                  # Environment template
├── 📄 .gitignore                    # Git ignore rules
│
├── 📄 main.py                       # Original entry point
├── 📄 aris_enhanced.py              # Enhanced ARIS ⭐ NEW
├── 📄 aris_launcher.py              # Launcher utility
│
├── 📄 gui.py                        # Original GUI
├── 📄 gui_enhanced.py               # Enhanced GUI
├── 📄 gui_text_mode.py              # Text mode GUI
├── 📄 gui_ultimate.py               # Ultimate GUI ⭐ NEW
│
├── 📄 jarvis_advanced.py            # Advanced features
├── 📄 jarvis_gui.py                 # JARVIS GUI
├── 📄 quick_start.py                # Quick start script
│
├── 📄 requirements.txt              # Python dependencies
├── 📄 docker-compose.yml            # Docker configuration
│
├── 🚀 start_aris.bat                # Start ARIS (basic)
├── 🚀 start_aris_easy.bat           # Easy start
├── 🚀 start_aris_background.vbs     # Background start
├── 🚀 start_ultimate.bat            # Ultimate launcher ⭐ NEW
├── 🚀 launch_file_manager.bat       # File manager launcher ⭐ NEW
├── 🚀 launch_aris_gui.bat           # GUI launcher
│
├── 🔧 install_all.bat               # Install dependencies
├── 🔧 setup_aris.bat                # Setup script
├── 🔧 install_aris_service.ps1      # Service installer
├── 🔧 add_to_startup.ps1            # Startup configuration
├── 🔧 create_shortcut.ps1           # Shortcut creator
│
├── 📚 README.md                     # Main documentation
├── 📚 FEATURES.md                   # Feature list
├── 📚 ULTIMATE_FEATURES.md          # Ultimate features ⭐ NEW
├── 📚 FILE_MANAGEMENT_GUIDE.md      # File management docs ⭐ NEW
├── 📚 PROJECT_STRUCTURE.md          # This file ⭐ NEW
├── 📚 GETTING_STARTED.md            # Getting started guide
├── 📚 JARVIS_GUIDE.md               # JARVIS guide
├── 📚 HOW_TO_RUN.md                 # How to run
├── 📚 HOW_TO_START_ARIS.md          # Start guide
├── 📚 USAGE_GUIDE.md                # Usage guide
├── 📚 API_SETUP_GUIDE.md            # API setup
├── 📚 QUICK_REFERENCE.md            # Quick reference
├── 📚 ALL_COMMANDS.md               # All commands
├── 📚 CHANGELOG.md                  # Change log
├── 📚 WHATS_NEW.md                  # What's new
│
└── 📄 aris_project.bundle           # Project bundle

```

## Module Descriptions

### 🎯 Core System

**core/** - Essential ARIS functionality
- Speech recognition and synthesis
- Wake word detection
- Natural language understanding
- Core management

**orion_engine/** - AI brain
- Command routing and processing
- Memory and learning
- Personality system
- NLP processing

### 🆕 New Features (Ultimate Edition)

**plugins/** - Plugin system
- Dynamic plugin loading
- Extensible architecture
- Example plugins included

**extensions/** - Custom extensions
- User-defined commands
- Custom actions and triggers

**scheduler/** - Advanced scheduling
- Task scheduling with recurrence
- Natural language time parsing
- Background execution

**conversation/** - Context management
- Conversation history
- Context awareness
- User preference learning

**smart_home/** - Smart home control
- Device discovery and control
- Multiple integration support
- Scene management

**localization/** - Multi-language
- Translation management
- Language switching
- Locale files

**web_dashboard/** - Web interface
- Flask-based dashboard
- Real-time WebSocket communication
- Remote control capability

**file_manager/** - File management
- Voice-controlled file operations
- GUI file browser
- Programmatic API
- Operation history

### 📡 Integrations

**api/** - External API integrations
- Weather, news, stocks
- Email, calendar
- Wikipedia, YouTube
- Sports scores

**commands/** - Command modules
- System commands
- Web commands
- AI commands
- Games and entertainment
- Multi-language commands
- Automation commands

### 🎨 User Interfaces

**GUI Options:**
1. `gui.py` - Original GUI
2. `gui_enhanced.py` - Enhanced GUI
3. `gui_text_mode.py` - Text mode
4. `gui_ultimate.py` - Ultimate GUI (recommended)
5. `file_manager/gui_file_manager.py` - File manager GUI

**Web Interface:**
- `web_dashboard/app.py` - Web dashboard

### 📊 Data Storage

**data/** - Persistent data
- SQLite database
- JSON configuration files
- Task and event storage
- Conversation history
- Operation logs

**logs/** - Application logs
- Main application log
- Enhanced features log
- Error tracking

### 🔧 Configuration

**config/** - Configuration files
- Environment variables
- Settings
- Custom commands

### 🚀 Launchers

**Batch Files:**
- `start_ultimate.bat` - Main launcher (recommended)
- `launch_file_manager.bat` - File manager
- `start_aris_easy.bat` - Simple start
- `install_all.bat` - Dependency installer

**PowerShell Scripts:**
- `install_aris_service.ps1` - Service installation
- `add_to_startup.ps1` - Startup configuration
- `create_shortcut.ps1` - Shortcut creation

## Entry Points

### Main Applications

1. **Enhanced ARIS** (Recommended)
   ```bash
   python aris_enhanced.py
   ```
   Full-featured voice assistant with all new features

2. **Ultimate GUI** (Recommended)
   ```bash
   python gui_ultimate.py
   ```
   Complete GUI with all features integrated

3. **Web Dashboard**
   ```bash
   python web_dashboard/app.py
   ```
   Browser-based control panel

4. **File Manager**
   ```bash
   python file_manager/gui_file_manager.py
   ```
   Standalone file management GUI

5. **Original ARIS**
   ```bash
   python main.py
   ```
   Original voice assistant

### Quick Launchers

```bash
# Windows
start_ultimate.bat          # Choose interface
launch_file_manager.bat     # File manager only
start_aris_easy.bat         # Simple start

# Direct Python
python aris_enhanced.py     # Enhanced voice mode
python gui_ultimate.py      # Ultimate GUI
```

## Feature Locations

| Feature | Location | Entry Point |
|---------|----------|-------------|
| Plugin System | `plugins/` | Integrated in `aris_enhanced.py` |
| Custom Commands | `extensions/` | Integrated in `aris_enhanced.py` |
| Advanced Scheduler | `scheduler/` | Integrated in `aris_enhanced.py` |
| Conversation Context | `conversation/` | Integrated in `aris_enhanced.py` |
| Smart Home | `smart_home/` | Integrated in `aris_enhanced.py` |
| Multi-Language | `localization/` | Integrated in `aris_enhanced.py` |
| Web Dashboard | `web_dashboard/` | `python web_dashboard/app.py` |
| File Management | `file_manager/` | `python file_manager/gui_file_manager.py` |

## Configuration Files

| File | Purpose | Format |
|------|---------|--------|
| `config/config.env` | Environment variables | ENV |
| `config/custom_commands.json` | User commands | JSON |
| `data/scheduled_tasks.json` | Scheduled tasks | JSON |
| `data/conversation_history.json` | Chat history | JSON |
| `data/file_operations_history.json` | File ops log | JSON |
| `localization/locales/*.json` | Translations | JSON |

## Dependencies

See `requirements.txt` for complete list. Key dependencies:

**Core:**
- SpeechRecognition
- pyttsx3
- openai
- PyAudio
- python-dotenv

**Web:**
- flask
- flask-socketio

**Utilities:**
- requests
- beautifulsoup4
- psutil

## Development

### Adding New Features

1. **Plugin** - Create in `plugins/`
2. **Command Module** - Create in `commands/`
3. **API Integration** - Create in `api/`
4. **Extension** - Create in `extensions/`

### Testing

```bash
python tests/test_all_features.py
python tests/test_aris.py
python tests/test_voice_simple.py
```

## Documentation

| Document | Description |
|----------|-------------|
| `README.md` | Project overview |
| `ULTIMATE_FEATURES.md` | All new features |
| `FILE_MANAGEMENT_GUIDE.md` | File management docs |
| `PROJECT_STRUCTURE.md` | This file |
| `FEATURES.md` | Feature list |
| `USAGE_GUIDE.md` | Usage instructions |
| `API_SETUP_GUIDE.md` | API configuration |
| `GETTING_STARTED.md` | Getting started |

## Best Practices

1. **Use Enhanced ARIS** - `aris_enhanced.py` for full features
2. **Use Ultimate GUI** - `gui_ultimate.py` for best experience
3. **Check Logs** - `logs/` for debugging
4. **Review History** - Operation logs for tracking
5. **Backup Config** - Save `config/` and `data/`

## Quick Reference

```bash
# Install
pip install -r requirements.txt

# Run (choose one)
python aris_enhanced.py      # Voice mode
python gui_ultimate.py       # GUI mode
python web_dashboard/app.py  # Web mode

# Or use launcher
start_ultimate.bat           # Windows launcher
```

---

**ARIS Project Structure - Everything in One Place** 📁
