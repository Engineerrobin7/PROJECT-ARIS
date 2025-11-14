# How to Run ARIS - Complete Guide

## 🚀 Quick Start (Easiest Way)

### Windows Users:
```bash
start_aris_easy.bat
```
This will show you a menu to choose your preferred mode.

---

## 📋 Three Ways to Run ARIS

### 1. **Text Mode** (RECOMMENDED - Most Reliable)
Type your commands instead of speaking them.

```bash
python gui_text_mode.py
```

**Advantages:**
- ✅ Always works
- ✅ No microphone issues
- ✅ Fast and responsive
- ✅ Perfect for testing

**Example Session:**
```
You: what time is it
ARIS: The current time is 14:30 and the date is 2025-11-12.

You: tell me a joke
ARIS: Why did the programmer quit his job? Because he didn't get arrays!

You: flip a coin
ARIS: The coin landed on: Heads!
```

---

### 2. **GUI Mode** (Visual Interface)
Beautiful graphical interface with both text and voice options.

```bash
python gui_enhanced.py
```

**Features:**
- Modern dark theme
- Chat-style interface
- Type OR use voice button
- Scrollable history
- Status indicators

**How to Use:**
1. Type in the text box at bottom
2. Press Enter or click "Send"
3. OR click "🎤 Voice" button to speak
4. View responses in the chat window

---

### 3. **Voice Mode** (Always Listening)
Traditional voice assistant that waits for wake word.

```bash
python main.py
```

**How to Use:**
1. Say "wake up aris"
2. Wait for "I'm listening"
3. Speak your command
4. Press Ctrl+C to exit

**Note:** Requires good microphone and quiet environment.

---

## 🔧 Troubleshooting Voice Issues

If voice commands aren't working:

### Test Your Microphone:
```bash
python test_voice_simple.py
```

### Common Issues:

**1. "Could not understand audio"**
- Speak louder and clearer
- Reduce background noise
- Check microphone settings
- Try text mode instead

**2. Microphone not detected**
- Check Windows sound settings
- Ensure microphone is default device
- Grant microphone permissions
- Restart the application

**3. Voice recognized but command not executed**
- This is now FIXED in the latest version
- Make sure you're using the updated `gui_enhanced.py`

### Quick Fix:
If voice isn't working well, **use Text Mode** - it has all the same features!

---

## 📝 Example Commands

### Basic Commands
```
what time is it
what's the date
hello aris
thank you
```

### Fun & Games
```
tell me a joke
flip a coin
roll the dice
let's play a number game
magic 8 ball will I succeed
```

### Translation
```
translate hello to spanish
how do you say goodbye in french
teach me basic german
```

### Information (Requires API Keys)
```
what's the weather in london
latest news
wikipedia search for python
what's apple stock price
check bitcoin price
```

### System Commands
```
open notepad
open calculator
open browser
```

---

## ⚙️ Configuration

### API Keys (Optional but Recommended)

Edit `config/config.env`:

```env
# Required for AI features
OPENAI_API_KEY=your_key_here

# Optional - for specific features
WEATHER_API_KEY=your_key_here
NEWS_API_KEY=your_key_here
```

See `API_SETUP_GUIDE.md` for detailed setup.

---

## 🎯 Recommended Setup

**For Best Experience:**

1. **Start with Text Mode**
   ```bash
   python gui_text_mode.py
   ```

2. **Test all features** without voice issues

3. **Configure API keys** for weather, news, etc.

4. **Try GUI Mode** for visual interface

5. **Test voice** if you want voice features
   ```bash
   python test_voice_simple.py
   ```

---

## 💡 Pro Tips

1. **Text Mode is fastest** - No waiting for voice recognition
2. **GUI Mode looks best** - Great for demos
3. **Voice Mode is coolest** - But needs good setup
4. **Type 'help'** in text mode for command list
5. **Check logs** at `logs/aris.log` for errors

---

## 🆘 Still Having Issues?

### Check Installation:
```bash
python quick_start.py
```

### View Logs:
```bash
type logs\aris.log
```

### Test Components:
```bash
python test_all_features.py
```

---

## 📚 More Help

- **FEATURES.md** - Complete feature list
- **USAGE_GUIDE.md** - Detailed usage instructions
- **API_SETUP_GUIDE.md** - API configuration
- **QUICK_REFERENCE.md** - Quick command reference

---

## ✅ Summary

**Easiest Way to Start:**
```bash
python gui_text_mode.py
```

**Most Features:**
```bash
python gui_enhanced.py
```

**Coolest (if working):**
```bash
python main.py
```

**Choose what works best for you!** 🚀
