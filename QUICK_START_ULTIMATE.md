# ARIS Ultimate - Quick Start Guide

## ⚡ 30-Second Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run ARIS
start_ultimate.bat

# OR directly:
python gui_ultimate.py
```

That's it! You're ready to go! 🚀

---

## 🎯 Choose Your Interface

### 1. Ultimate GUI (Recommended) ⭐
```bash
python gui_ultimate.py
```
**Best for:** Complete control with visual interface

**Features:**
- Chat interface
- Voice input button
- Plugin management
- Smart home control
- Task scheduling
- File management
- Settings

### 2. Enhanced Voice Mode
```bash
python aris_enhanced.py
```
**Best for:** Hands-free operation

**Features:**
- Wake word detection
- Continuous listening
- All voice commands
- Background operation

### 3. Web Dashboard
```bash
python web_dashboard/app.py
# Open: http://localhost:5000
```
**Best for:** Remote control from any device

**Features:**
- Browser-based
- Real-time updates
- Mobile-friendly
- Remote access

### 4. File Manager
```bash
python file_manager/gui_file_manager.py
# OR
launch_file_manager.bat
```
**Best for:** File organization

**Features:**
- Visual file browser
- Drag and drop
- Search and organize
- Batch operations

---

## 🎤 Essential Voice Commands

### Basic
```
"What time is it?"
"What's the weather?"
"Tell me a joke"
"Search Google for [query]"
```

### File Management
```
"List files"
"Create file notes.txt"
"Delete file old.txt"
"Organize files"
"Search for report"
```

### Smart Home
```
"Turn on living room light"
"Set thermostat to 72"
"Discover smart devices"
```

### Scheduling
```
"Remind me to call John in 1 hour"
"Schedule meeting tomorrow at 3 PM"
"Show my upcoming tasks"
```

### System
```
"Open Notepad"
"Close Calculator"
"Shutdown computer"
```

---

## 📁 Project Structure (Simplified)

```
ARIS/
├── aris_enhanced.py          # Enhanced voice mode ⭐
├── gui_ultimate.py            # Ultimate GUI ⭐
├── start_ultimate.bat         # Launcher ⭐
│
├── plugins/                   # Plugin system
├── extensions/                # Custom commands
├── scheduler/                 # Task scheduling
├── conversation/              # Context & history
├── smart_home/                # Device control
├── localization/              # Multi-language
├── web_dashboard/             # Web interface
├── file_manager/              # File management ⭐
│
├── config/                    # Configuration
├── data/                      # Data storage
└── logs/                      # Log files
```

---

## 🔧 Quick Configuration

### 1. Set Your Name
Edit `config/config.env`:
```env
USER_NAME=YourName
WAKE_WORD=wake up aris
```

### 2. Add API Keys (Optional)
```env
OPENAI_API_KEY=your_key_here
WEATHER_API_KEY=your_key_here
NEWS_API_KEY=your_key_here
```

### 3. Create Custom Command
Edit `config/custom_commands.json`:
```json
{
  "hello aris": {
    "action_type": "speak",
    "action_data": "Hello! How can I help?",
    "response": "Hello! How can I help?"
  }
}
```

---

## 🎮 GUI Quick Tour

### Main Tab 💬
- Type or speak commands
- View conversation history
- Voice input button

### Plugins Tab 🔌
- View loaded plugins
- Enable/disable plugins
- Refresh plugin list

### Smart Home Tab 🏠
- Discover devices
- Control devices
- View device status

### Scheduler Tab ⏰
- Add new tasks
- View upcoming tasks
- Set reminders

### Custom Commands Tab ⚡
- Create custom commands
- View existing commands
- Edit triggers

### Files Tab 📁
- Open file manager
- View voice commands
- Quick file operations

### Settings Tab ⚙️
- Change language
- View statistics
- Configure preferences

---

## 🚀 Common Tasks

### Task 1: Schedule a Reminder
**GUI:**
1. Go to "⏰ Scheduler" tab
2. Enter task name
3. Enter time (e.g., "in 1 hour")
4. Click "Add Task"

**Voice:**
```
"Remind me to take a break in 1 hour"
```

### Task 2: Organize Files
**GUI:**
1. Go to "📁 Files" tab
2. Click "Open File Manager"
3. Click "🔧 Organize"

**Voice:**
```
"Organize files"
```

### Task 3: Control Smart Device
**GUI:**
1. Go to "🏠 Smart Home" tab
2. Click "Discover Devices"
3. Click device control button

**Voice:**
```
"Turn on living room light"
```

### Task 4: Create Custom Command
**GUI:**
1. Go to "⚡ Custom Commands" tab
2. Enter trigger phrase
3. Enter response
4. Click "Add Command"

**Voice:**
```
"[Your custom trigger]"
```

### Task 5: Search Files
**GUI:**
1. Go to "📁 Files" tab
2. Click "Open File Manager"
3. Enter search query
4. Press Enter

**Voice:**
```
"Search for report"
```

---

## 💡 Pro Tips

1. **Use Wake Word** - Say "wake up aris" for hands-free
2. **Check Logs** - View `logs/` for debugging
3. **Organize Daily** - Use "organize files" regularly
4. **Create Shortcuts** - Add custom commands for frequent tasks
5. **Use Web Dashboard** - Control from phone/tablet
6. **Schedule Recurring** - Set daily/weekly reminders
7. **Explore Plugins** - Check example plugin for ideas
8. **Multi-Language** - Switch languages anytime

---

## 🐛 Quick Troubleshooting

### Voice Not Working
```bash
# Check microphone
# Reinstall PyAudio
pip install --upgrade pyaudio
```

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### GUI Not Opening
```bash
# Check tkinter
python -m tkinter
```

### Web Dashboard Error
```bash
# Install Flask
pip install flask flask-socketio
```

---

## 📚 Learn More

**Essential Docs:**
- `COMPLETE_FEATURE_SUMMARY.md` - All features
- `FILE_MANAGEMENT_GUIDE.md` - File operations
- `ULTIMATE_FEATURES.md` - Detailed guides
- `PROJECT_STRUCTURE.md` - Project layout

**Quick Reference:**
- `ALL_COMMANDS.md` - All voice commands
- `USAGE_GUIDE.md` - Usage examples
- `API_SETUP_GUIDE.md` - API configuration

---

## 🎯 Your First 5 Minutes

**Minute 1:** Launch
```bash
start_ultimate.bat
# Choose option 1 (Ultimate GUI)
```

**Minute 2:** Try Voice
- Click "🎤 Voice" button
- Say: "What time is it?"

**Minute 3:** Explore Tabs
- Click through each tab
- See what's available

**Minute 4:** Create Custom Command
- Go to "⚡ Custom Commands"
- Add: "hello" → "Hello there!"

**Minute 5:** Test File Manager
- Go to "📁 Files"
- Click "Open File Manager"
- Browse your files

---

## 🌟 Feature Checklist

Try these features:

- [ ] Voice command
- [ ] Custom command
- [ ] Schedule reminder
- [ ] File organization
- [ ] Smart device control
- [ ] Web dashboard
- [ ] Plugin system
- [ ] Multi-language
- [ ] File search
- [ ] Conversation history

---

## 🎊 You're All Set!

**You now have:**
✅ Complete AI assistant
✅ Voice control
✅ Multiple interfaces
✅ File management
✅ Smart home control
✅ Task scheduling
✅ Custom commands
✅ Plugin system

**Start exploring:**
```bash
start_ultimate.bat
```

**Need help?**
- Check documentation files
- Review examples in code
- Check logs for errors

---

**Welcome to ARIS Ultimate!** 🚀

Your complete AI assistant is ready to use.

Enjoy! 🎉
