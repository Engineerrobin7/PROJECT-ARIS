# core/speech_output.py
"""
Converts text to speech (TTS).
"""
import pyttsx3

class TTSEngine:
    """Speaks the given text using a TTS engine."""
    def __init__(self, voice=None, rate=150):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)
        print("TTS Engine initialized.")

    def speak(self, text):
        """
        Converts the given text to speech.
        """
        print(f"ARIS: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
