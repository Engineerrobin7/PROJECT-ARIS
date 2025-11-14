"""
Multi-language support and localization
"""
import json
import os
import logging
from typing import Dict, Any

class LanguageManager:
    """Manages multi-language support for ARIS"""
    
    def __init__(self, locale_dir: str = "localization/locales"):
        self.locale_dir = locale_dir
        self.current_language = "en"
        self.translations: Dict[str, Dict[str, str]] = {}
        self.logger = logging.getLogger('LanguageManager')
        self.load_translations()
    
    def load_translations(self):
        """Load all available translations"""
        os.makedirs(self.locale_dir, exist_ok=True)
        
        # Load existing translation files
        for filename in os.listdir(self.locale_dir):
            if filename.endswith('.json'):
                lang_code = filename[:-5]
                try:
                    with open(os.path.join(self.locale_dir, filename), 'r', encoding='utf-8') as f:
                        self.translations[lang_code] = json.load(f)
                except Exception as e:
                    self.logger.error(f"Failed to load {filename}: {e}")
        
        # Create default English if not exists
        if 'en' not in self.translations:
            self.translations['en'] = self._get_default_english()
            self.save_translation('en')
    
    def set_language(self, language_code: str) -> bool:
        """Set the current language"""
        if language_code in self.translations:
            self.current_language = language_code
            self.logger.info(f"Language set to {language_code}")
            return True
        return False
    
    def get_text(self, key: str, **kwargs) -> str:
        """Get translated text for a key"""
        translation = self.translations.get(self.current_language, {}).get(key)
        
        if not translation:
            # Fallback to English
            translation = self.translations.get('en', {}).get(key, key)
        
        # Format with kwargs if provided
        if kwargs:
            try:
                translation = translation.format(**kwargs)
            except:
                pass
        
        return translation
    
    def save_translation(self, language_code: str):
        """Save translations for a language"""
        filepath = os.path.join(self.locale_dir, f"{language_code}.json")
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.translations[language_code], f, indent=2, ensure_ascii=False)
        except Exception as e:
            self.logger.error(f"Failed to save translation: {e}")
    
    def add_translation(self, language_code: str, key: str, value: str):
        """Add a new translation"""
        if language_code not in self.translations:
            self.translations[language_code] = {}
        
        self.translations[language_code][key] = value
        self.save_translation(language_code)
    
    def get_available_languages(self) -> Dict[str, str]:
        """Get list of available languages"""
        return {
            "en": "English",
            "es": "Español",
            "fr": "Français",
            "de": "Deutsch",
            "it": "Italiano",
            "pt": "Português",
            "ru": "Русский",
            "ja": "日本語",
            "zh": "中文",
            "ko": "한국어",
            "ar": "العربية"
        }
    
    def _get_default_english(self) -> Dict[str, str]:
        """Get default English translations"""
        return {
            # Greetings
            "greeting_morning": "Good morning",
            "greeting_afternoon": "Good afternoon",
            "greeting_evening": "Good evening",
            "greeting_general": "Hello",
            
            # Status messages
            "listening": "I'm listening",
            "processing": "Processing your request",
            "error": "I encountered an error",
            "success": "Done",
            
            # Commands
            "command_not_understood": "I didn't understand that command",
            "command_executed": "Command executed successfully",
            
            # System
            "startup": "ARIS online. How can I assist you?",
            "shutdown": "Goodbye",
            "wake_word_detected": "Yes?",
            
            # Features
            "weather_checking": "Checking the weather",
            "news_fetching": "Fetching the latest news",
            "reminder_set": "Reminder set for {time}",
            "timer_started": "Timer started for {duration}",
            
            # Errors
            "no_internet": "No internet connection available",
            "api_error": "API service unavailable",
            "permission_denied": "Permission denied",
            
            # Smart home
            "device_not_found": "Device not found",
            "device_controlled": "Device controlled successfully",
            "scene_activated": "Scene activated"
        }
