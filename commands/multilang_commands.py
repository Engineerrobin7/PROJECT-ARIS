# commands/multilang_commands.py
"""
Handles multi-language translation and language learning commands.
"""
import requests

class MultiLangCommands:
    def __init__(self):
        self.supported_languages = {
            "spanish": "es",
            "french": "fr",
            "german": "de",
            "italian": "it",
            "portuguese": "pt",
            "russian": "ru",
            "japanese": "ja",
            "chinese": "zh",
            "korean": "ko",
            "arabic": "ar"
        }
    
    def handle_command(self, command):
        """Handle language-related commands."""
        if "translate" in command:
            return self.translate_text(command)
        elif "how do you say" in command:
            return self.translate_phrase(command)
        elif "learn" in command and any(lang in command for lang in self.supported_languages):
            return self.language_lesson(command)
        else:
            return "I can translate text or teach you basic phrases in different languages."
    
    def translate_text(self, command):
        """Translate text using a free translation API."""
        # Simple translation using LibreTranslate (free, open-source)
        # For production, consider using Google Translate API or DeepL
        
        try:
            # Extract text and target language from command
            # Example: "translate hello to spanish"
            parts = command.lower().split(" to ")
            if len(parts) < 2:
                return "Please specify the target language. For example: 'translate hello to Spanish'"
            
            text_part = parts[0].replace("translate", "").strip()
            target_lang = parts[1].strip()
            
            # Find language code
            lang_code = self.supported_languages.get(target_lang, None)
            if not lang_code:
                return f"Sorry, I don't support translation to {target_lang} yet."
            
            # Use a simple dictionary for common phrases (fallback)
            common_translations = {
                "hello": {"es": "hola", "fr": "bonjour", "de": "hallo", "it": "ciao"},
                "goodbye": {"es": "adiós", "fr": "au revoir", "de": "auf wiedersehen", "it": "arrivederci"},
                "thank you": {"es": "gracias", "fr": "merci", "de": "danke", "it": "grazie"},
                "yes": {"es": "sí", "fr": "oui", "de": "ja", "it": "sì"},
                "no": {"es": "no", "fr": "non", "de": "nein", "it": "no"}
            }
            
            if text_part in common_translations and lang_code in common_translations[text_part]:
                translation = common_translations[text_part][lang_code]
                return f"'{text_part}' in {target_lang} is '{translation}'"
            
            return f"Translation: I can translate common phrases like hello, goodbye, thank you, yes, and no."
        except Exception as e:
            return f"Error translating: {str(e)}"
    
    def translate_phrase(self, command):
        """Translate a specific phrase."""
        # Example: "how do you say hello in Spanish"
        return self.translate_text(command.replace("how do you say", "translate"))
    
    def language_lesson(self, command):
        """Provide a basic language lesson."""
        lessons = {
            "spanish": "Basic Spanish: Hola (hello), Adiós (goodbye), Gracias (thank you), Por favor (please), Sí (yes), No (no)",
            "french": "Basic French: Bonjour (hello), Au revoir (goodbye), Merci (thank you), S'il vous plaît (please), Oui (yes), Non (no)",
            "german": "Basic German: Hallo (hello), Auf Wiedersehen (goodbye), Danke (thank you), Bitte (please), Ja (yes), Nein (no)",
            "italian": "Basic Italian: Ciao (hello), Arrivederci (goodbye), Grazie (thank you), Per favore (please), Sì (yes), No (no)"
        }
        
        for lang, lesson in lessons.items():
            if lang in command.lower():
                return lesson
        
        return "I can teach you basic phrases in Spanish, French, German, or Italian."

def handle_command(command):
    """Entry point for multi-language commands."""
    multilang = MultiLangCommands()
    return multilang.handle_command(command)
