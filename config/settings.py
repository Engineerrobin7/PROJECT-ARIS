# config/settings.py
"""
Default configurations for ARIS (e.g., voice rate, wake word, etc.).
These can be overridden by environment variables.
"""

# Speech Output (TTS) settings
DEFAULT_VOICE_RATE = 170  # Words per minute
DEFAULT_VOICE_VOLUME = 1.0  # 0.0 to 1.0

# Wake Word settings
DEFAULT_WAKE_WORD = "aris"
WAKE_WORD_SENSITIVITY = 0.5  # 0.0 to 1.0

# Speech Recognition settings
LANGUAGE = "en-US"  # Language code for speech recognition
TIMEOUT = 5  # Seconds to listen for a command before timing out

# Logging settings
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = "logs/aris.log"

# NLP settings
MAX_TOKENS = 150  # Maximum tokens for GPT responses
TEMPERATURE = 0.7  # Randomness of GPT responses (0.0 to 1.0)
